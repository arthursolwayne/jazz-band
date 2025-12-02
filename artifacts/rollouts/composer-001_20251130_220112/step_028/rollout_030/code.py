
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in D
bass_notes = [
    # D (2nd fret, 6th string) = 65
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    # C# (1st fret, 6th string) = 64
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    # B (open 5th string) = 62
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),
    # C (2nd fret, 5th string) = 67
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: D7 on beat 2
piano_notes = [
    # D7: D, F#, A, C
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
]
# Bar 3: G7 on beat 2
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=78, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=73, start=3.375, end=3.75),
])
# Bar 4: C7 on beat 2
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
])
piano.notes.extend(piano_notes)

# Sax: Melody in bars 2-4
# Bar 2: Start of motif
sax_notes = [
    # D (67) on beat 1
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),
    # F# (71) on beat 2
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25),
    # A (74) on beat 3
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.625),
    # D (67) on beat 4
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),
]
# Bar 3: Continue motif
sax_notes.extend([
    # G (71) on beat 1
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),
    # B (74) on beat 2
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75),
    # D (67) on beat 3
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),
    # F# (71) on beat 4
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),
])
# Bar 4: Finish motif
sax_notes.extend([
    # A (74) on beat 1
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.875),
    # D (67) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),
    # F# (71) on beat 3
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),
    # D (67) on beat 4
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),
])
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
