
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (root) on beat 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F (chromatic approach to G) on & of 1
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.0),
    # G2 (fifth) on beat 2
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # F# (chromatic approach to G) on & of 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    # D2 (root) on beat 3
    pretty_midi.Note(velocity=90, pitch=38, start=2.5625, end=2.9375),
    # F (chromatic approach to G) on & of 3
    pretty_midi.Note(velocity=80, pitch=41, start=2.9375, end=3.125),
    # G2 (fifth) on beat 4
    pretty_midi.Note(velocity=90, pitch=43, start=3.125, end=3.5),
    # F# (chromatic approach to G) on & of 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=3.5),  # D4
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=3.5),  # F4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=3.5),  # A4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=3.5),  # C4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start with a short motif on bar 2 (Dm7)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # C4
    # Leave it hanging, come back and finish it on bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (root) on beat 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    # F (chromatic approach to G) on & of 1
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.5625),
    # G2 (fifth) on beat 2
    pretty_midi.Note(velocity=90, pitch=43, start=3.5625, end=3.9375),
    # F# (chromatic approach to G) on & of 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    # D2 (root) on beat 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),
    # F (chromatic approach to G) on & of 3
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.6875),
    # G2 (fifth) on beat 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.6875, end=5.0625),
    # F# (chromatic approach to G) on & of 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=4.5),  # F4
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (root) on beat 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    # F (chromatic approach to G) on & of 1
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.0625),
    # G2 (fifth) on beat 2
    pretty_midi.Note(velocity=90, pitch=43, start=5.0625, end=5.4375),
    # F# (chromatic approach to G) on & of 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    # D2 (root) on beat 3
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
    # F (chromatic approach to G) on & of 3
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),
    # G2 (fifth) on beat 4
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),
    # F# (chromatic approach to G) on & of 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=6.0),  # B4
]
piano.notes.extend(piano_notes)

# Bar 4: Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
