
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass: D2 (D2 is MIDI 38) to G2 (G2 is MIDI 43) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0),  # C4
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4 (MIDI 62), F#4 (MIDI 67), A4 (MIDI 69), G4 (MIDI 67)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Everyone in (3.0 - 4.5s)
# Bass: G2 (MIDI 43) to B2 (MIDI 46) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125),  # B2
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),  # A#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Bm7 (B D F# A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5),  # F#5
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5),  # A5
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# B4 (MIDI 67), D5 (MIDI 71), F#5 (MIDI 74), E5 (MIDI 72)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # F#5
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # E5
]
sax.notes.extend(sax_notes)

# Bar 4: Everyone in (4.5 - 6.0s)
# Bass: B2 (MIDI 46) to D3 (MIDI 49) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875),  # B2
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25),  # C3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625),  # D3
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),  # C#3 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Dmaj7 (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4 (MIDI 62), F#4 (MIDI 67), A4 (MIDI 69), G4 (MIDI 67)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G4
]
sax.notes.extend(sax_notes)

# Drums: kick=36, snare=38, hihat=42
# Bar 4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
