
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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=60, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5),
    # Bar 4 continuation
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=2.75),
    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=63, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=66, start=3.5, end=3.75),
]
piano.notes.extend(piano_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62), Eb (63), F (64), D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
