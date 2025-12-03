
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# D2 = 38, G2 = 43
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=2.0),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.5),  # A2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (G4, A4, D5, F#5)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # F#5
]
piano.notes.extend(piano_notes)

# Bar 2: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax, one short motif, make it sing
# D4 (62), F#4 (66), G4 (67), A4 (69), Bb4 (70), D5 (74)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # F#4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# D2 = 38, G2 = 43
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.25),  # G2
    pretty_midi.Note(velocity=90, pitch=45, start=3.25, end=3.5),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.75),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.0),  # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Dm7 (F#4, A4, D5, F5)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),  # F5
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625),
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax, continue the motif
# F#4 (66), G4 (67), A4 (69), Bb4 (70)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=110, pitch=70, start=3.75, end=4.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# D2 = 38, G2 = 43
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.75),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.75, end=5.0),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=5.0, end=5.25),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.5),  # A2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dmaj7 (F#4, A4, D5, F#5)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # F#5
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.75, end=4.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0),
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax, finish the motif
# D5 (74), F#4 (66), G4 (67), A4 (69)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
