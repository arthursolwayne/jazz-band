
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bars 2-4 (1.5 - 6.0s)

# Bass: Walking line in Fm (F2, Bb2, Eb2, Ab2, etc.)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # Bb2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # D2 (chromatic approach)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125),  # Ab2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Bb2 (chromatic approach)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # D2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # Bb4
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # Eb4 (Ab4)
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4, G4, Ab4, F4 (quarter note each)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=55, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=110, pitch=57, start=3.0, end=3.75),  # Ab4
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=5.25),  # F4 (return)
    pretty_midi.Note(velocity=110, pitch=55, start=5.25, end=6.0),  # G4 (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.8125, end=3.0),
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.3125, end=4.5),
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.8125, end=6.0),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
