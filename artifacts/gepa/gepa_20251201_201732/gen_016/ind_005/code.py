
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

# Bass: Walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> chromatic approach to G2 (43)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),
    # Bar 3: G2 (43) -> chromatic approach to A2 (45)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),
    # Bar 4: A2 (45) -> chromatic approach to D3 (50)
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),  # D3
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),  # F#3
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.0),  # A3
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.0),  # C4
]
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.5),  # G3
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.5),  # Bb3
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),  # F4
])
# Bar 4: A7 (A-C#-E-G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=5.0),  # A3
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # C#4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # G4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif (D4 - F#4 - D4)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # F#4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Continue the pattern for bars 2-4
for i in range(0, len(drum_notes), 12):
    start = 1.5 + i / 12 * 3.0
    for note in drum_notes[i:i+12]:
        new_note = pretty_midi.Note(note.velocity, note.pitch, start + note.start, start + note.end)
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
