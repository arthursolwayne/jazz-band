
import mido
from mido import Message, MidiFile, MidiTrack

# Constants
BPM = 160
BEAT = 60 / BPM  # 0.375 seconds per beat
BAR = 4 * BEAT  # 1.5 seconds per bar
TIME_SIGNATURE = (4, 4)
TEMPO = BPM * 1000  # in microseconds per beat

# MIDI note values
# Fm7: F, Ab, C, Eb
# Fm: F, Ab, D, Eb (if using drop 2 voicings)
# We'll use open voicings for Diane's piano
# Marcus: walking bass line (D2-G2, MIDI 38-43)
# Diane: open voicings, different chord each bar.
# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
# You: one short motif, haunting, starting on bar 1, ending on bar 4.

# MIDI file setup
mid = MidiFile()
track1 = MidiTrack()
track2 = MidiTrack()
track3 = MidiTrack()
track4 = MidiTrack()
mid.tracks.append(track1)
mid.tracks.append(track2)
mid.tracks.append(track3)
mid.tracks.append(track4)

# Set tempo
track1.append(mido.MetaMessage('set_tempo', tempo=TEMPO, time=0))
track1.append(mido.MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notes_per_quarter=8, time=0))

# Helper function to add a note
def add_note(track, note, time, duration=0.5, velocity=100):
    start = mido.tick2time(time, ticks_per_beat=960)
    end = start + mido.tick2time(duration * 960, ticks_per_beat=960)
    track.append(Message('note_on', note=note, velocity=velocity, time=start))
    track.append(Message('note_off', note=note, velocity=velocity, time=end - start))

# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time is in ticks (each beat = 960 ticks, so each eighth = 480, 1/16 = 240, etc.)

# Bar 1 (0-960 ticks)
track4.append(Message('note_on', note=36, velocity=100, time=0))  # Kick on 1 (beat 0)
track4.append(Message('note_off', note=36, velocity=100, time=960 - 0))
track4.append(Message('note_on', note=38, velocity=100, time=480))  # Snare on 2
track4.append(Message('note_off', note=38, velocity=100, time=960 - 480))
track4.append(Message('note_on', note=42, velocity=80, time=0))  # Hihat on 1
track4.append(Message('note_off', note=42, velocity=80, time=480))
track4.append(Message('note_on', note=42, velocity=80, time=480))  # Hihat on 2
track4.append(Message('note_off', note=42, velocity=80, time=960 - 480))
track4.append(Message('note_on', note=42, velocity=80, time=960))  # Hihat on 3
track4.append(Message('note_off', note=42, velocity=80, time=1440 - 960))
track4.append(Message('note_on', note=42, velocity=80, time=1440))  # Hihat on 4
track4.append(Message('note_off', note=42, velocity=80, time=1920 - 1440))

# Bar 2: Everyone in. Diane: Fm7 (F, Ab, C, Eb) open voicing
track2.append(Message('note_on', note=65, velocity=100, time=960))  # F (MIDI 65)
track2.append(Message('note_off', note=65, velocity=100, time=480))
track2.append(Message('note_on', note=68, velocity=100, time=960))  # Ab (MIDI 68)
track2.append(Message('note_off', note=68, velocity=100, time=480))
track2.append(Message('note_on', note=72, velocity=100, time=960))  # C (MIDI 72)
track2.append(Message('note_off', note=72, velocity=100, time=480))
track2.append(Message('note_on', note=69, velocity=100, time=960))  # Eb (MIDI 69)
track2.append(Message('note_off', note=69, velocity=100, time=480))

# Marcus: Walking bass line (Fm7) - D2-G2, roots and fifths with chromatic approaches
track3.append(Message('note_on', note=38, velocity=90, time=960))  # D (root, Fm7)
track3.append(Message('note_off', note=38, velocity=90, time=480))
track3.append(Message('note_on', note=43, velocity=90, time=1440))  # G (fifth of F)
track3.append(Message('note_off', note=43, velocity=90, time=480))
track3.append(Message('note_on', note=42, velocity=90, time=1920))  # F (chromatic approach)
track3.append(Message('note_off', note=42, velocity=90, time=480))
track3.append(Message('note_on', note=38, velocity=90, time=2400))  # D (root again)
track3.append(Message('note_off', note=38, velocity=90, time=480))

# Bar 3: Diane: Ab7 (Ab, C, Eb, G) open voicing
track2.append(Message('note_on', note=68, velocity=100, time=1920))  # Ab
track2.append(Message('note_off', note=68, velocity=100, time=480))
track2.append(Message('note_on', note=72, velocity=100, time=1920))  # C
track2.append(Message('note_off', note=72, velocity=100, time=480))
track2.append(Message('note_on', note=69, velocity=100, time=1920))  # Eb
track2.append(Message('note_off', note=69, velocity=100, time=480))
track2.append(Message('note_on', note=71, velocity=100, time=1920))  # G
track2.append(Message('note_off', note=71, velocity=100, time=480))

# Marcus: Walking bass line (Ab7) - Ab (MIDI 57), D (MIDI 50), chromatic approach (F# MIDI 66)
track3.append(Message('note_on', note=57, velocity=90, time=1920))  # Ab
track3.append(Message('note_off', note=57, velocity=90, time=480))
track3.append(Message('note_on', note=50, velocity=90, time=2400))  # D (fifth of Ab)
track3.append(Message('note_off', note=50, velocity=90, time=480))
track3.append(Message('note_on', note=66, velocity=90, time=2880))  # F# (chromatic)
track3.append(Message('note_off', note=66, velocity=90, time=480))
track3.append(Message('note_on', note=57, velocity=90, time=3360))  # Ab
track3.append(Message('note_off', note=57, velocity=90, time=480))

# Bar 4: Diane: Cm7 (C, Eb, G, Bb) open voicing
track2.append(Message('note_on', note=72, velocity=100, time=2880))  # C
track2.append(Message('note_off', note=72, velocity=100, time=480))
track2.append(Message('note_on', note=69, velocity=100, time=2880))  # Eb
track2.append(Message('note_off', note=69, velocity=100, time=480))
track2.append(Message('note_on', note=71, velocity=100, time=2880))  # G
track2.append(Message('note_off', note=71, velocity=100, time=480))
track2.append(Message('note_on', note=67, velocity=100, time=2880))  # Bb
track2.append(Message('note_off', note=67, velocity=100, time=480))

# Marcus: Walking bass line (Cm7) - C (MIDI 60), G (MIDI 67), chromatic approach (Bb MIDI 62)
track3.append(Message('note_on', note=60, velocity=90, time=2880))  # C
track3.append(Message('note_off', note=60, velocity=90, time=480))
track3.append(Message('note_on', note=67, velocity=90, time=3360))  # G (fifth of Cm)
track3.append(Message('note_off', note=67, velocity=90, time=480))
track3.append(Message('note_on', note=62, velocity=90, time=3840))  # Bb (chromatic)
track3.append(Message('note_off', note=62, velocity=90, time=480))
track3.append(Message('note_on', note=60, velocity=90, time=4320))  # C
track3.append(Message('note_off', note=60, velocity=90, time=480))

# You: Tenor sax - one short motif, haunting, starts on bar 1, ends on bar 4
# Motif: F (MIDI 65), Ab (MIDI 68), Bb (MIDI 67), rest (hang), then F again
# Bar 1: F
track1.append(Message('note_on', note=65, velocity=100, time=0))
track1.append(Message('note_off', note=65, velocity=100, time=480))

# Bar 2: Ab
track1.append(Message('note_on', note=68, velocity=100, time=960))
track1.append(Message('note_off', note=68, velocity=100, time=480))

# Bar 3: Bb, rest
track1.append(Message('note_on', note=67, velocity=100, time=1920))
track1.append(Message('note_off', note=67, velocity=100, time=240))

# Bar 4: F again
track1.append(Message('note_on', note=65, velocity=100, time=2160))
track1.append(Message('note_off', note=65, velocity=100, time=480))

# Save the MIDI file
mid.save('dante_russo_intro.mid')
print("MIDI file generated: 'dante_russo_intro.mid'")
