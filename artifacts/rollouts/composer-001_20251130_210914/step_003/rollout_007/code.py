
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
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=54, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.25, end=4.5),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=63, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Bar 2: Fm7 on beat 2
note = pretty_midi.Note(velocity=100, pitch=53, start=1.75, end=2.0)  # Bb
note2 = pretty_midi.Note(velocity=100, pitch=48, start=1.75, end=2.0)  # F
note3 = pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=2.0)  # G
note4 = pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0)  # C
piano.notes.extend([note, note2, note3, note4])

# Bar 3: Fm7 on beat 2
note = pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5)  # Bb
note2 = pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.5)  # F
note3 = pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.5)  # G
note4 = pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5)  # C
piano.notes.extend([note, note2, note3, note4])

# Bar 4: Fm7 on beat 2
note = pretty_midi.Note(velocity=100, pitch=53, start=4.75, end=5.0)  # Bb
note2 = pretty_midi.Note(velocity=100, pitch=48, start=4.75, end=5.0)  # F
note3 = pretty_midi.Note(velocity=100, pitch=50, start=4.75, end=5.0)  # G
note4 = pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0)  # C
piano.notes.extend([note, note2, note3, note4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - Bb - F (melodic minor)
note = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75)  # F
note2 = pretty_midi.Note(velocity=100, pitch=55, start=1.75, end=2.0)  # G
note3 = pretty_midi.Note(velocity=100, pitch=56, start=2.0, end=2.25)  # Ab
note4 = pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5)  # F
note5 = pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25)  # F
note6 = pretty_midi.Note(velocity=100, pitch=55, start=3.25, end=3.5)  # G
note7 = pretty_midi.Note(velocity=100, pitch=56, start=3.5, end=3.75)  # Ab
note8 = pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.0)  # F
note9 = pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75)  # F
note10 = pretty_midi.Note(velocity=100, pitch=55, start=4.75, end=5.0)  # G
note11 = pretty_midi.Note(velocity=100, pitch=56, start=5.0, end=5.25)  # Ab
note12 = pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5)  # F
note13 = pretty_midi.Note(velocity=100, pitch=53, start=5.5, end=5.75)  # F
note14 = pretty_midi.Note(velocity=100, pitch=55, start=5.75, end=6.0)  # G
note15 = pretty_midi.Note(velocity=100, pitch=56, start=6.0, end=6.25)  # Ab
note16 = pretty_midi.Note(velocity=100, pitch=53, start=6.0, end=6.25)  # F (end on F)
sax.notes.extend([note, note2, note3, note4, note5, note6, note7, note8, note9, note10, note11, note12, note13, note14, note15, note16])

# Drums: Bar 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
