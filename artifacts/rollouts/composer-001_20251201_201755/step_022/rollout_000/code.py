
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
# Bass: D2 (38) to G2 (43), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.125), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.5),   # G2
    pretty_midi.Note(velocity=80, pitch=41, start=2.5, end=2.875),   # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),   # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),   # F#4
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=2.0),   # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0),   # C#4
    # Bar 3: Em7 (E, G, B, D)
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.5),   # E4
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.5),   # G4
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.5),   # B4
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),   # G3 (root)
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),   # G4
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=3.0),   # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=3.0),   # D4
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=3.0),   # F4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),   # E4
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),   # E4
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),   # F#4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (38) to G2 (43), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),   # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.625, end=4.0),   # G2
    pretty_midi.Note(velocity=80, pitch=41, start=4.0, end=4.375),   # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: Em7 (E, G, B, D)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),   # E4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5),   # G4
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.5),   # B4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5),   # G3 (root)
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=4.0),   # G4
    pretty_midi.Note(velocity=90, pitch=76, start=3.5, end=4.0),   # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=4.0),   # D4
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=4.0),   # F4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),   # E4
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),   # E4
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),   # F#4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (38) to G2 (43), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),   # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.125), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.125, end=5.5),   # G2
    pretty_midi.Note(velocity=80, pitch=41, start=5.5, end=5.875),   # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),   # G4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=5.0),   # B4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=5.0),   # D4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.0),   # F4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),   # E4
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),   # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),   # E4
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),   # G4
]
sax.notes.extend(sax_notes)

# Drums: kick=36, snare=38, hihat=42
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.6875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
