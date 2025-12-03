
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=110, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=110, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=110, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=110, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Start of the melody
# Bass: D2 (D)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),   # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: D7 in open voicing
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=2.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C#4
]
# Bar 3: Bm7
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # B3
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.5),  # F#4
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # C#4
]
# Bar 4: G7
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G3
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=3.0),  # B4
    pretty_midi.Note(velocity=90, pitch=77, start=2.5, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # F#4
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax: Motif
# Start with a short motif, leave it hanging, come back and finish
# Motif: D4, F4, B4, D5 (in quarter notes)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=81, start=2.625, end=3.0),   # D5
    # Repeat the first two notes in the last bar to finish the motif
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.875),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=2.875, end=3.0),   # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
