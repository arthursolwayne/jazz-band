
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice.
# In F, root motion: F -> G -> A -> Bb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875), # F (F4)
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25), # G (G4)
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # A (A4)
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0), # F (F4)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375), # G (G4)
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75), # A (A4)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # D (D4) - chromatic approach
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5), # F (F4)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875), # G (G4)
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25), # A (A4)
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.625), # Bb (Bb4)
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0), # F (F4)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25), # G
    # Bar 3 (2.25 - 3.0)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0), # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0), # E
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0), # G
    # Bar 4 (3.0 - 3.75)
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.75), # A
    # Bar 4 (3.75 - 4.5)
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5), # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5), # E
    pretty_midi.Note(velocity=90, pitch=78, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=90, pitch=80, start=4.125, end=4.5), # Bb
    # Bar 4 (4.5 - 5.25)
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.25), # C
    # Bar 4 (5.25 - 6.0)
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0), # E
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0), # G
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0), # Bb
    pretty_midi.Note(velocity=90, pitch=83, start=5.625, end=6.0), # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (F4), Ab (Ab4), Bb (Bb4) in 1st bar, then repeat ending in 4th bar
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0), # G
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
# Hi-hat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
