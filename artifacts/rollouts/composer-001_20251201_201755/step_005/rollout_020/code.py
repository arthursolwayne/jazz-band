
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=2.0),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=2.0, end=2.5),   # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=3.0),   # G2
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.5),   # G2
    pretty_midi.Note(velocity=90, pitch=41, start=3.5, end=4.0),   # F2
    pretty_midi.Note(velocity=90, pitch=38, start=4.0, end=4.5),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=5.0),   # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=5.0, end=5.5),   # G2
    pretty_midi.Note(velocity=90, pitch=43, start=5.5, end=6.0),   # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (F, A, D, G)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),   # F4
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=2.0),   # A4
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),   # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),   # G4

    # Bar 3: G7 (B, D, G, F)
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=3.0),   # B4
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0),   # D4
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),   # G4
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=3.0),   # F4

    # Bar 4: Cm7 (E, G, C, E)
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=4.0),   # E4
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=4.0),   # G4
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=4.0),   # C4
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=4.0),   # E5

    # Bar 4: Resolve to Dm7 again
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.0),   # F4
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=5.0),   # A4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),   # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),   # G4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Start with a D4 (62), then a Bb4 (66), then a G4 (67), then a D5 (72)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0),  # D5
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
