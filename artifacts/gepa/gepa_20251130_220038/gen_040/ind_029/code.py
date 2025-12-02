
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1 (0.0 - 1.5s): Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # seconds per bar at 160 BPM

# Bar 1
drum_notes = [
    # Kick on beat 1
    pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375),
    # Snare on beat 2
    pretty_midi.Note(velocity=100, pitch=snare, start=0.75, end=1.125),
    # Kick on beat 3
    pretty_midi.Note(velocity=100, pitch=kick, start=1.125, end=1.5),
    # Snare on beat 4
    pretty_midi.Note(velocity=100, pitch=snare, start=1.5, end=1.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=hihat, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s): Full quartet
# Sax: Motif - Fm7 -> G -> Ab -> Bb -> Fm7
# Fm7: F, Ab, Bb, Db
# G: G
# Ab: Ab
# Bb: Bb
# Fm7: F, Ab, Bb, Db

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm (F, G, Ab, A)
# Chromatic approach: F -> G -> Ab -> A
# Each note on beat 1, 2, 3, 4 of bar 2

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4 with 7th chords
# Fm7 on beat 2, Fm7 on beat 4

piano_notes = [
    # Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # Db
    # Fm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3 (3.0 - 4.5s): Full quartet
# Sax: Repeat the motif, but with a slight variation or hold on last note
# Fm7 -> G -> Ab -> Bb -> Fm7

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.5),   # F (held)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4 again
piano_notes = [
    # Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # Db
    # Fm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4 (4.5 - 6.0s): Full quartet
# Sax: Repeat motif again but end on a sustained F for resolution
# Fm7 -> G -> Ab -> Bb -> Fm7

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=6.0),   # F (held)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4 again
piano_notes = [
    # Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # Db
    # Fm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 and 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 3
for i in range(2):
    start = 3.0 + i * 1.5
    # Kick on beat 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=start, end=start + 0.375))
    # Snare on beat 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=start + 0.75, end=start + 1.125))
    # Kick on beat 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=start + 1.125, end=start + 1.5))
    # Snare on beat 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=start + 1.5, end=start + 1.875))
    # Hihat
    for j in range(4):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=start + j * 0.375, end=start + j * 0.375 + 0.375))

# Bar 4
for i in range(2):
    start = 4.5 + i * 1.5
    # Kick on beat 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=start, end=start + 0.375))
    # Snare on beat 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=start + 0.75, end=start + 1.125))
    # Kick on beat 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=start + 1.125, end=start + 1.5))
    # Snare on beat 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=start + 1.5, end=start + 1.875))
    # Hihat
    for j in range(4):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=start + j * 0.375, end=start + j * 0.375 + 0.375))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
