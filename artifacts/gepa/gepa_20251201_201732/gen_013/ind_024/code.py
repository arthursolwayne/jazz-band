
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=1.75, end=2.0),  # F2
    pretty_midi.Note(velocity=100, pitch=51, start=2.0, end=2.25),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.5),  # A2
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.75),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=2.75, end=3.0),  # F2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5),  # F2
    pretty_midi.Note(velocity=100, pitch=52, start=3.5, end=3.75),  # E2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.0),  # A2
    pretty_midi.Note(velocity=100, pitch=50, start=4.0, end=4.25),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=4.25, end=4.5),  # F2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=4.75, end=5.0),  # F2
    pretty_midi.Note(velocity=100, pitch=51, start=5.0, end=5.25),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.5),  # A2
    pretty_midi.Note(velocity=100, pitch=50, start=5.5, end=5.75),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=5.75, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F Ab C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # C5
    
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # F5

    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # Bb4
]
piano.notes.extend(piano_notes)

# Drums: same pattern for bars 2-4
for i in range(1, 3):
    for note in drum_notes:
        new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 1.5 * i, note.end + 1.5 * i)
        drums.notes.append(new_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F4, Eb4, D4 (half note, half note, quarter note, eighth note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=4.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25)  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
