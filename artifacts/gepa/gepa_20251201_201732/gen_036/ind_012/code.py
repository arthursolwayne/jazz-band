
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass line: walking line in Fm (F, Bb, Eb, Ab)
# Root and fifth with chromatic approaches
# Bar 2: F - Eb - F - Gb
bass_notes_bar2 = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),  # F2
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # Gb2
]
# Bar 3: Bb - Ab - Bb - B
bass_notes_bar3 = [
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125),  # Bb2
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),  # B2
]
# Bar 4: Eb - D - Eb - E
bass_notes_bar4 = [
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25),  # D2
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.625),  # Eb2
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # E2
]
bass.notes.extend(bass_notes_bar2 + bass_notes_bar3 + bass_notes_bar4)

# Piano: open voicings, different chord each bar, resolve on last
# Bar 2: Fm7
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Ab4
]
# Bar 3: Cm7
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # Bb4
]
# Bar 4: Fm7 (resolve back to Fm)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Ab4
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: G - A - Bb (Fm scale, 2nd, 3rd, 4th)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75),  # G4 (return)
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # Bb4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
