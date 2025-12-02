
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.5),  # G
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=76, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=77, start=2.75, end=3.0),  # A#
    pretty_midi.Note(velocity=80, pitch=75, start=3.0, end=3.25),  # G#
    pretty_midi.Note(velocity=80, pitch=73, start=3.25, end=3.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=80, pitch=72, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=80, pitch=74, start=4.25, end=4.5),  # G
    # Bar 4 continuation
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=77, start=4.75, end=5.0),  # A#
    pretty_midi.Note(velocity=80, pitch=75, start=5.0, end=5.25),  # G#
    pretty_midi.Note(velocity=80, pitch=73, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=5.75, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=70, pitch=74, start=1.5, end=1.75),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=70, pitch=74, start=2.5, end=2.75),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=70, pitch=74, start=3.5, end=3.75),  # Bb
    # Bar 4 continuation
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=70, pitch=74, start=4.5, end=4.75),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (69), A (72), Bb (71), F (69) - with a slight delay on the last note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
