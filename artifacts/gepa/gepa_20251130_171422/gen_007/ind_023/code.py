
import mido
from mido import Message, MidiFile, MidiTrack

# Tempo and Time
BPM = 160
PPQ = 960  # Pulses Per Quarter Note (standard)
BEAT_DURATION = mido.tick2second(PPQ, BPM)
BAR_DURATION = 4 * BEAT_DURATION  # 4 beats per bar

# Create a MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo
track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(BPM), time=0))

# Constants for timing
TICK_PER_EIGHT = PPQ // 2
TICK_PER_SIXTEENTH = PPQ // 4

# ---- Little Ray (Drums) - Bar 1 (0-1.5s)
track.append(Message('note_on', note=38, velocity=100, time=0))  # Kick on beat 1
track.append(Message('note_off', note=38, velocity=100, time=PPQ))  # Kick on beat 1

track.append(Message('note_on', note=46, velocity=100, time=0))  # Snare on beat 2
track.append(Message('note_off', note=46, velocity=100, time=PPQ))  # Snare on beat 2

track.append(Message('note_on', note=42, velocity=80, time=0))  # Hi-hat on beat 3
track.append(Message('note_off', note=42, velocity=80, time=PPQ))  # Hi-hat on beat 3

track.append(Message('note_on', note=46, velocity=100, time=0))  # Snare on beat 4
track.append(Message('note_off', note=46, velocity=100, time=PPQ))  # Snare on beat 4

track.append(Message('note_on', note=42, velocity=80, time=0))  # Hi-hat on beat 1
track.append(Message('note_off', note=42, velocity=80, time=TICK_PER_SIXTEENTH))  # Hi-hat on beat 1
track.append(Message('note_on', note=42, velocity=80, time=0))  # Hi-hat on beat 2
track.append(Message('note_off', note=42, velocity=80, time=TICK_PER_SIXTEENTH))  # Hi-hat on beat 2
track.append(Message('note_on', note=42, velocity=80, time=0))  # Hi-hat on beat 3
track.append(Message('note_off', note=42, velocity=80, time=TICK_PER_SIXTEENTH))  # Hi-hat on beat 3
track.append(Message('note_on', note=42, velocity=80, time=0))  # Hi-hat on beat 4
track.append(Message('note_off', note=42, velocity=80, time=TICK_PER_SIXTEENTH))  # Hi-hat on beat 4

# ---- Bars 2-4: Full Band Entry

# You - Tenor Sax (Motif)
# F -> Bb -> D -> F (F7 chord, but with a chromatic twist)
# Play on beat 1 of bar 2, leave it hanging, then resolve on beat 3 of bar 4

# Bar 2, beat 1: F (72)
track.append(Message('note_on', note=72, velocity=100, time=BAR_DURATION))
track.append(Message('note_off', note=72, velocity=100, time=TICK_PER_SIXTEENTH))

# Bar 2, beat 2: Bb (70)
track.append(Message('note_on', note=70, velocity=100, time=0))
track.append(Message('note_off', note=70, velocity=100, time=TICK_PER_SIXTEENTH))

# Bar 2, beat 3: D (67)
track.append(Message('note_on', note=67, velocity=100, time=0))
track.append(Message('note_off', note=67, velocity=100, time=TICK_PER_SIXTEENTH))

# Bar 2, beat 4: Rest — leave it hanging

# Bar 3, beat 1: F (72) again (subtle resolution)
track.append(Message('note_on', note=72, velocity=100, time=BAR_DURATION * 2))
track.append(Message('note_off', note=72, velocity=100, time=TICK_PER_SIXTEENTH))

# Bar 4, beat 3: D (67), leading back to F
track.append(Message('note_on', note=67, velocity=100, time=BAR_DURATION * 3))
track.append(Message('note_off', note=67, velocity=100, time=TICK_PER_SIXTEENTH))

# Marcus - Bass Line (Walking, chromatic approaches)
# Bar 2, beat 1: E (64) - chromatic approach to F
track.append(Message('note_on', note=64, velocity=80, time=BAR_DURATION))
track.append(Message('note_off', note=64, velocity=80, time=TICK_PER_SIXTEENTH))

# Bar 2, beat 2: F (72)
track.append(Message('note_on', note=72, velocity=80, time=0))
track.append(Message('note_off', note=72, velocity=80, time=TICK_PER_SIXTEENTH))

# Bar 2, beat 3: G (71)
track.append(Message('note_on', note=71, velocity=80, time=0))
track.append(Message('note_off', note=71, velocity=80, time=TICK_PER_SIXTEENTH))

# Bar 2, beat 4: A (74)
track.append(Message('note_on', note=74, velocity=80, time=0))
track.append(Message('note_off', note=74, velocity=80, time=TICK_PER_SIXTEENTH))

# Bar 3, beat 1: A (74)
track.append(Message('note_on', note=74, velocity=80, time=BAR_DURATION * 2))
track.append(Message('note_off', note=74, velocity=80, time=TICK_PER_SIXTEENTH))

# Bar 3, beat 2: Bb (70)
track.append(Message('note_on', note=70, velocity=80, time=0))
track.append(Message('note_off', note=70, velocity=80, time=TICK_PER_SIXTEENTH))

# Bar 3, beat 3: C (60) - chromatic approach to D
track.append(Message('note_on', note=60, velocity=80, time=0))
track.append(Message('note_off', note=60, velocity=80, time=TICK_PER_SIXTEENTH))

# Bar 3, beat 4: D (67)
track.append(Message('note_on', note=67, velocity=80, time=0))
track.append(Message('note_off', note=67, velocity=80, time=TICK_PER_SIXTEENTH))

# Diane - Piano - 7th chords, comp on 2 and 4
# Bar 2, beat 2: F7 (F, A, C, Eb)
track.append(Message('note_on', note=72, velocity=100, time=BAR_DURATION))
track.append(Message('note_off', note=72, velocity=100, time=TICK_PER_SIXTEENTH))

track.append(Message('note_on', note=74, velocity=100, time=0))
track.append(Message('note_off', note=74, velocity=100, time=TICK_PER_SIXTEENTH))

track.append(Message('note_on', note=76, velocity=100, time=0))
track.append(Message('note_off', note=76, velocity=100, time=TICK_PER_SIXTEENTH))

track.append(Message('note_on', note=70, velocity=100, time=0))
track.append(Message('note_off', note=70, velocity=100, time=TICK_PER_SIXTEENTH))

# Bar 2, beat 4: F7 again (same chord)
track.append(Message('note_on', note=72, velocity=100, time=BAR_DURATION * 2))
track.append(Message('note_off', note=72, velocity=100, time=TICK_PER_SIXTEENTH))

track.append(Message('note_on', note=74, velocity=100, time=0))
track.append(Message('note_off', note=74, velocity=100, time=TICK_PER_SIXTEENTH))

track.append(Message('note_on', note=76, velocity=100, time=0))
track.append(Message('note_off', note=76, velocity=100, time=TICK_PER_SIXTEENTH))

track.append(Message('note_on', note=70, velocity=100, time=0))
track.append(Message('note_off', note=70, velocity=100, time=TICK_PER_SIXTEENTH))

# Bar 3, beat 2: F7 again
track.append(Message('note_on', note=72, velocity=100, time=BAR_DURATION * 3))
track.append(Message('note_off', note=72, velocity=100, time=TICK_PER_SIXTEENTH))

track.append(Message('note_on', note=74, velocity=100, time=0))
track.append(Message('note_off', note=74, velocity=100, time=TICK_PER_SIXTEENTH))

track.append(Message('note_on', note=76, velocity=100, time=0))
track.append(Message('note_off', note=76, velocity=100, time=TICK_PER_SIXTEENTH))

track.append(Message('note_on', note=70, velocity=100, time=0))
track.append(Message('note_off', note=70, velocity=100, time=TICK_PER_SIXTEENTH))

# Save the MIDI file
mid.save('dante_cellar_intro.mid')
print("MIDI file saved as 'dante_cellar_intro.mid'")
