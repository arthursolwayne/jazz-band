
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # C3 (fifth of Fm)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # Bb2
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # C3
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625),  # Bb2
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0)   # C3
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875), # Bb4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875)  # C5
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625)  # F4
]
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # C5
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375), # Eb5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # G5
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375)  # Bb5
]
# Add them to piano
piano.notes.extend(piano_notes_bar2)
piano.notes.extend(piano_notes_bar3)
piano.notes.extend(piano_notes_bar4)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - Bb - C, staggered
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),   # F4
    pretty_midi.Note(velocity=110, pitch=57, start=2.25, end=2.625),  # Ab4
    pretty_midi.Note(velocity=110, pitch=58, start=3.0, end=3.375),   # Bb4
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875)    # C5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
