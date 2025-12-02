
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody starts
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # F (4th)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # G (5th)
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # E (3rd)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # F (4th)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=3.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2 (1.875)
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # G
    # F7 on beat 4 (2.625)
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0), # G
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # F (4th)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # G (5th)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # E (3rd)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # F (4th)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2 (3.375)
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75), # G
    # F7 on beat 4 (4.125)
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5), # F
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5), # A
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5), # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5), # G
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # F (4th)
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # G (5th)
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # E (3rd)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # F (4th)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2 (4.875)
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # G
    # F7 on beat 4 (5.625)
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0), # F
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0), # A
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0), # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0), # G
]

for note in piano_notes:
    piano.notes.append(note)

# Drums for bar 3 and 4
for bar in [3, 4]:
    start_time = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.0, end=start_time + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.0, end=start_time + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.375, end=start_time + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.75, end=start_time + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.125, end=start_time + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.5, end=start_time + 1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.875, end=start_time + 2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 2.25, end=start_time + 2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 2.625, end=start_time + 3.0),
]

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
