
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

# Bar 2: Full quartet begins
# Sax - Dm motif: D, F, G, Bb (sax in Bb, so D = C, F = E, G = F#, Bb = A)
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625),  # C (D in Dm)
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # E (F in Dm)
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=1.875),  # F# (G in Dm)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # A (Bb in Dm)
]
sax.notes.extend(sax_notes)

# Bass - Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # F (Dm root)
    pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75),  # G (chromatic)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=1.875),  # D (Dm root)
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),   # A (chromatic)
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # F (Dm7)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),  # A (Dm7)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625),  # G (Dm7)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.625),  # C (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # F (Dm7)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # A (Dm7)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),  # G (Dm7)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),  # C (Dm7)
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax continues motif (Bar 3)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.375),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5),  # A
]
sax.notes.extend(sax_notes)

# Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=2.375, end=2.5),   # F
]
bass.notes.extend(bass_notes)

# Piano continues comping
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=2.875),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax completes the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=2.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Bass completes walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0),   # A
]
bass.notes.extend(bass_notes)

# Piano completes comping
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.625),  # C
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
