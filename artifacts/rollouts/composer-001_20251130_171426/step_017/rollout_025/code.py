
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus bass: walking line, chromatic approaches, never the same note twice
# Dm7 chord: D, F, A, C
# Walking line in D Dorian
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),  # D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # E
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5),  # D
    # Bar 4 continuation
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # D
]
bass.notes.extend(bass_notes)

# Diane piano: 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
# Comp on 2 and 4
piano_notes = [
    # Bar 2: comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),  # C
]
piano.notes.extend(piano_notes)

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Dante sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D, Eb, F, C (with a little chromaticism)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=105, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=105, pitch=60, start=2.25, end=2.5),  # C
    # Leave it hanging
    pretty_midi.Note(velocity=105, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=105, pitch=63, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=105, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=105, pitch=60, start=3.25, end=3.5),  # C
    # Finish it
    pretty_midi.Note(velocity=105, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=105, pitch=63, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=105, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=105, pitch=60, start=4.25, end=4.5),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
