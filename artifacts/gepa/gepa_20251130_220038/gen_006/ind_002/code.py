
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass - walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    # Bar 3: F7
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    # Bar 4: Gm7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F
]
piano.notes.extend(piano_notes)

# Drums - continue pattern
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax - motif: Dm7 to G7 to Gm7
# Bar 2: Dm7 - start on D, ascend to F
note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)  # D
note2 = pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0)  # F
note3 = pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25)  # G
note4 = pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5)  # Bb
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: G7 - resolve to Bb
note5 = pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25)  # G
note6 = pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.5)  # Bb
note7 = pretty_midi.Note(velocity=110, pitch=74, start=3.5, end=3.75)  # D
note8 = pretty_midi.Note(velocity=110, pitch=70, start=3.75, end=4.0)  # F
sax.notes.extend([note5, note6, note7, note8])

# Bar 4: Gm7 - end on Bb
note9 = pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75)  # G
note10 = pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0)  # Bb
note11 = pretty_midi.Note(velocity=110, pitch=74, start=5.0, end=5.25)  # D
note12 = pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5)  # F
sax.notes.extend([note9, note10, note11, note12])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
