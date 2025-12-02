
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) to G2 (MIDI 43) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last chord (Dm7)
piano_notes = [
    # Bar 2: Dm7 (F, A, D, G)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # G4
]
piano.notes.extend(piano_notes)

# Sax: One motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: C2 (MIDI 36) to F2 (MIDI 41) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),  # C2
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # Eb2
]
bass.notes.extend(bass_notes)

# Piano: Bm7 (D, F#, B, E) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=4.5),  # F#4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # B4
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # C4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: A2 (MIDI 40) to D2 (MIDI 38) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=90, pitch=39, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=90, pitch=37, start=5.625, end=6.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (Bb, D, G, B) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # B4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
