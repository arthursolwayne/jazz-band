
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=100, pitch=46, start=1.75, end=2.0),  # F#3
    pretty_midi.Note(velocity=100, pitch=44, start=2.0, end=2.25),  # E3
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.5),  # F3
    pretty_midi.Note(velocity=100, pitch=47, start=2.5, end=2.75),  # G3
    pretty_midi.Note(velocity=100, pitch=48, start=2.75, end=3.0),  # G#3
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.25),  # F#3
    pretty_midi.Note(velocity=100, pitch=45, start=3.25, end=3.5),  # F3
    pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=3.75),  # D3
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.0),  # E3
    pretty_midi.Note(velocity=100, pitch=45, start=4.0, end=4.25),  # F3
    pretty_midi.Note(velocity=100, pitch=47, start=4.25, end=4.5),  # G3
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.75),  # G#3
    pretty_midi.Note(velocity=100, pitch=46, start=4.75, end=5.0),  # F#3
    pretty_midi.Note(velocity=100, pitch=45, start=5.0, end=5.25),  # F3
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.5),  # D3
    pretty_midi.Note(velocity=100, pitch=44, start=5.5, end=5.75),  # E3
    pretty_midi.Note(velocity=100, pitch=45, start=5.75, end=6.0),  # F3
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),  # E4
    # Bar 3: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # C4
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0),  # F4
]
piano.notes.extend(piano_notes)

# Dante: Melody - the intro that makes Wayne lean forward
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),  # E4
    pretty_midi.Note(velocity=110, pitch=68, start=2.75, end=3.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # G#4
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75),  # E4
    pretty_midi.Note(velocity=110, pitch=68, start=3.75, end=4.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25),  # A4
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.5),  # G#4
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.25),  # E4
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.5),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.75),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=5.75, end=6.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.875),  # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.375),  # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.875),  # Snare on 4
]
# Hihat on every eighth
for i in range(1.5, 6.0, 0.375):
    if i % 0.75 != 0:  # Skip on 1 and 3
        pretty_midi.Note(velocity=100, pitch=42, start=i, end=i + 0.375)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
