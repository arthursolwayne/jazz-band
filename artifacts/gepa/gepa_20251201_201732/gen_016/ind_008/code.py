
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4 (but bar ends at 1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass (Marcus): Walking line D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, resolve on the last bar
# Bar 2: Dm7 (F, A, D, G)
# Bar 3: G7 (B, D, G, B)
# Bar 4: Cm7 (Eb, G, C, E)
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25), # D4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25), # G4

    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0), # B4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0), # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0), # B4

    # Bar 4 (3.0 - 3.75s, but only comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # Eb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # C4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # E4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F4

    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # G4

    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
