
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),  # E2 (chromatic approach)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),  # E2 (chromatic approach)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),  # E2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0),  # E5

    # Bar 3 (3.0 - 4.5s) - Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # C5

    # Bar 4 (4.5 - 6.0s) - G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0),  # F5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F4 (65), G4 (67), A4 (72), Bb4 (71), C5 (69)
sax_notes = [
    # Start the motif (Bar 2, 1.5 - 1.875s)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),
    # Leave it hanging (Bar 2, 1.875 - 2.25s)
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),
    # Come back and finish it (Bar 4, 5.25 - 5.625s)
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
