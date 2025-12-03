
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
    # Kick on 1 and 3 (0.0, 1.125)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.25),
    # Snare on 2 and 4 (0.75, 1.75)
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=1.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus (walking line, roots and fifths with chromatic approaches)
# Dm7: D, A, F, C
# Bar 2: D (root), chromatic approach to A (Bb), A (fifth), chromatic approach to D (C#)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.625),  # D2
    pretty_midi.Note(velocity=70, pitch=40, start=1.625, end=1.75),  # Bb2
    pretty_midi.Note(velocity=90, pitch=43, start=1.75, end=1.875),  # A2
    pretty_midi.Note(velocity=70, pitch=41, start=1.875, end=2.0),  # C#2
    # Bar 3: F (root), chromatic approach to C (Db), C (fifth), chromatic approach to F (E)
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.125),  # F2
    pretty_midi.Note(velocity=70, pitch=40, start=2.125, end=2.25),  # Db2
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.375),  # C3
    pretty_midi.Note(velocity=70, pitch=46, start=2.375, end=2.5),  # E3
    # Bar 4: D (root), chromatic approach to A (Bb), A (fifth), chromatic approach to D (C#)
    pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.625),  # D2
    pretty_midi.Note(velocity=70, pitch=40, start=2.625, end=2.75),  # Bb2
    pretty_midi.Note(velocity=90, pitch=43, start=2.75, end=2.875),  # A2
    pretty_midi.Note(velocity=70, pitch=41, start=2.875, end=3.0),  # C#2
]
bass.notes.extend(bass_notes)

# Piano: Diane (open voicings, resolve on the last beat)
# Bar 2: Dm7
# Bar 3: F7
# Bar 4: Dm7
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # C5
    # Bar 3: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # C5
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # E5
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Dante (motif, one short phrase, sing it)
# Motif: D (start), F (chromatic), A (fifth), D (resolve)
# Bar 2: D, F#, A, D
# Bar 3: F, G, A, F
# Bar 4: D, F#, A, D (same as bar 2, but with a slight variation)
sax_notes = [
    # Bar 2: D, F#, A, D
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # D4
    # Bar 3: F, G, A, F
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.125),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.375),  # A4
    pretty_midi.Note(velocity=110, pitch=65, start=2.375, end=2.5),  # F4
    # Bar 4: D, F#, A, D (same as bar 2, but slightly delayed)
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.75),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),  # D4
]
sax.notes.extend(sax_notes)

# Add drum fills
# Bar 2: Fill on 3 (snare and hihat)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=1.9375),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),  # Hihat
]
drums.notes.extend(drum_notes)

# Bar 3: Fill on 3 (snare and hihat)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=2.375, end=2.4375),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5),  # Hihat
]
drums.notes.extend(drum_notes)

# Bar 4: Fill on 3 (snare and hihat)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=2.9375),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),  # Hihat
]
drums.notes.extend(drum_notes)

# Add final kick and snare on beat 4 of bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.875, end=2.9375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),  # Snare
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
