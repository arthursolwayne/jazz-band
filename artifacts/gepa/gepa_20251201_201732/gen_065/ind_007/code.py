
import mido
from mido import Message, MidiFile, MidiTrack
import time

# Constants
BPM = 160
TEMPO = 600000000 / BPM  # microseconds per beat
BAR_DURATION = 6.0  # 6 seconds per 4 bars
BEAT_DURATION = BAR_DURATION / 4  # seconds per beat
NOTE_DURATION = 0.375  # seconds per note (60 BPM is 1 beat per second, 160 BPM = 0.375s per beat)

# MIDI Note Mapping
# Fm7: F, Ab, C, Eb
F = 65  # F3
Ab = 68  # Ab3
C = 72  # C4
Eb = 74  # Eb4

# Tonic for Fm (F) and chromatic approach
F_flat = 64  # Fb (E)
F_sharp = 66  # F#

# Time signature: 4/4
# Key: F minor

# Create MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo
track.append(mido.MetaMessage('set_tempo', tempo=TEMPO, time=0))

# Bar 1: Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time in seconds
current_time = 0

# Kick on 1
track.append(Message('note_on', note=36, velocity=100, time=current_time))
track.append(Message('note_off', note=36, velocity=100, time=NOTE_DURATION))

current_time += NOTE_DURATION

# Hi-hat on 1 & 2 (eighth note)
track.append(Message('note_on', note=42, velocity=100, time=0))
track.append(Message('note_off', note=42, velocity=100, time=NOTE_DURATION / 2))
track.append(Message('note_on', note=42, velocity=100, time=NOTE_DURATION / 2))
track.append(Message('note_off', note=42, velocity=100, time=NOTE_DURATION / 2))

# Snare on 2
track.append(Message('note_on', note=38, velocity=100, time=current_time))
track.append(Message('note_off', note=38, velocity=100, time=NOTE_DURATION))

current_time += NOTE_DURATION

# Hi-hat on 3 & 4
track.append(Message('note_on', note=42, velocity=100, time=0))
track.append(Message('note_off', note=42, velocity=100, time=NOTE_DURATION / 2))
track.append(Message('note_on', note=42, velocity=100, time=NOTE_DURATION / 2))
track.append(Message('note_off', note=42, velocity=100, time=NOTE_DURATION / 2))

# Kick on 3
track.append(Message('note_on', note=36, velocity=100, time=current_time))
track.append(Message('note_off', note=36, velocity=100, time=NOTE_DURATION))

current_time += NOTE_DURATION

# Snare on 4
track.append(Message('note_on', note=38, velocity=100, time=current_time))
track.append(Message('note_off', note=38, velocity=100, time=NOTE_DURATION))

current_time += NOTE_DURATION

# Hi-hat on 1 (next bar)
track.append(Message('note_on', note=42, velocity=100, time=0))
track.append(Message('note_off', note=42, velocity=100, time=NOTE_DURATION / 2))
track.append(Message('note_on', note=42, velocity=100, time=NOTE_DURATION / 2))
track.append(Message('note_off', note=42, velocity=100, time=NOTE_DURATION / 2))

# Bar 2: Everyone in
# Diane — Fm7, open voicing (F, Ab, C, Eb), resolve on the last bar

# Diane: Bar 2 (Fm7)
diane_notes = [F, Ab, C, Eb]
for note in diane_notes:
    track.append(Message('note_on', note=note, velocity=100, time=0))
    track.append(Message('note_off', note=note, velocity=100, time=NOTE_DURATION * 2))

# Marcus — Walking bass line in Fm (F, Ab, C, Eb), with chromatic approach and rests
# Bar 2: F (root), Ab (flat 5), Eb (bass note), F (root)
# Marcus: F (36), Ab (39), Eb (31), F (36)
marcus_notes = [F, Ab, Eb, F]
for i, note in enumerate(marcus_notes):
    if i == 1:
        # rest for tension
        track.append(Message('note_on', note=note, velocity=100, time=0))
        track.append(Message('note_off', note=note, velocity=100, time=NOTE_DURATION))
    else:
        track.append(Message('note_on', note=note, velocity=100, time=0))
        track.append(Message('note_off', note=note, velocity=100, time=NOTE_DURATION))

# You — Tenor sax, one short motif, start it, leave it hanging, finish it
# Motif: F, Ab, F, rest (hang), F
# Motif over 4 beats (Bar 2), leave it hanging in bar 3

track.append(Message('note_on', note=F, velocity=100, time=0))
track.append(Message('note_off', note=F, velocity=100, time=NOTE_DURATION * 1))

track.append(Message('note_on', note=Ab, velocity=100, time=0))
track.append(Message('note_off', note=Ab, velocity=100, time=NOTE_DURATION * 1))

track.append(Message('note_on', note=F, velocity=100, time=0))
track.append(Message('note_off', note=F, velocity=100, time=NOTE_DURATION * 1))

# Leave it hanging on the last beat of bar 2
track.append(Message('note_on', note=F, velocity=100, time=0))
track.append(Message('note_off', note=F, velocity=100, time=NOTE_DURATION * 1))

# Bar 3: Diane — Cm7 (Ab, C, Eb, Gb)
diane_notes = [Ab, C, Eb, Gb]
for note in diane_notes:
    track.append(Message('note_on', note=note, velocity=100, time=0))
    track.append(Message('note_off', note=note, velocity=100, time=NOTE_DURATION * 2))

# Marcus — Walking line: Ab (39), Eb (31), C (36), Bb (37)
marcus_notes = [Ab, Eb, C, Bb]
for note in marcus_notes:
    track.append(Message('note_on', note=note, velocity=100, time=0))
    track.append(Message('note_off', note=note, velocity=100, time=NOTE_DURATION * 1))

# You — Motif returns with resolution
track.append(Message('note_on', note=F, velocity=100, time=0))
track.append(Message('note_off', note=F, velocity=100, time=NOTE_DURATION * 1))

track.append(Message('note_on', note=Ab, velocity=100, time=0))
track.append(Message('note_off', note=Ab, velocity=100, time=NOTE_DURATION * 1))

track.append(Message('note_on', note=F, velocity=100, time=0))
track.append(Message('note_off', note=F, velocity=100, time=NOTE_DURATION * 1))

track.append(Message('note_on', note=C, velocity=100, time=0))
track.append(Message('note_off', note=C, velocity=100, time=NOTE_DURATION * 1))

# Bar 4: Diane — Gm7 (Bb, D, F, G)
diane_notes = [Bb, D, F, G]
for note in diane_notes:
    track.append(Message('note_on', note=note, velocity=100, time=0))
    track.append(Message('note_off', note=note, velocity=100, time=NOTE_DURATION * 2))

# Marcus — Walking line: Bb (37), F (36), D (34), C (36)
marcus_notes = [Bb, F, D, C]
for note in marcus_notes:
    track.append(Message('note_on', note=note, velocity=100, time=0))
    track.append(Message('note_off', note=note, velocity=100, time=NOTE_DURATION * 1))

# Little Ray — Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4
track.append(Message('note_on', note=36, velocity=100, time=0))
track.append(Message('note_off', note=36, velocity=100, time=NOTE_DURATION))

track.append(Message('note_on', note=38, velocity=100, time=0))
track.append(Message('note_off', note=38, velocity=100, time=NOTE_DURATION))

track.append(Message('note_on', note=36, velocity=100, time=0))
track.append(Message('note_off', note=36, velocity=100, time=NOTE_DURATION))

track.append(Message('note_on', note=38, velocity=100, time=0))
track.append(Message('note_off', note=38, velocity=100, time=NOTE_DURATION))

# Save the MIDI file
mid.save('dante_intro.mid')
print("MIDI file 'dante_intro.mid' has been created.")
