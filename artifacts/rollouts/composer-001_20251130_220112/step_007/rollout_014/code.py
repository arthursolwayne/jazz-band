
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
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.5, end=2.75),  # G#
    pretty_midi.Note(velocity=90, pitch=49, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=52, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.0),  # G#
    pretty_midi.Note(velocity=90, pitch=52, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=90, pitch=54, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0),  # A#
    pretty_midi.Note(velocity=90, pitch=54, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.5),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Fm7 again
# Bb7 again

chord1 = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0)  # F
chord1_2 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0)  # Ab
chord1_3 = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0)  # C
chord1_4 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0)  # Eb

chord2 = pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.5)  # Bb
chord2_2 = pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5)  # D
chord2_3 = pretty_midi.Note(velocity=100, pitch=53, start=2.0, end=2.5)  # F
chord2_4 = pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.5)  # Ab

chord3 = pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.5)  # F
chord3_2 = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5)  # Ab
chord3_3 = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5)  # C
chord3_4 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5)  # Eb

chord4 = pretty_midi.Note(velocity=100, pitch=58, start=3.5, end=4.0)  # Bb
chord4_2 = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0)  # D
chord4_3 = pretty_midi.Note(velocity=100, pitch=53, start=3.5, end=4.0)  # F
chord4_4 = pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0)  # Ab

chord5 = pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=5.0)  # F
chord5_2 = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0)  # Ab
chord5_3 = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0)  # C
chord5_4 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0)  # Eb

chord6 = pretty_midi.Note(velocity=100, pitch=58, start=5.0, end=5.5)  # Bb
chord6_2 = pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.5)  # D
chord6_3 = pretty_midi.Note(velocity=100, pitch=53, start=5.0, end=5.5)  # F
chord6_4 = pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.5)  # Ab

piano.notes.extend([chord1, chord1_2, chord1_3, chord1_4,
                    chord2, chord2_2, chord2_3, chord2_4,
                    chord3, chord3_2, chord3_3, chord3_4,
                    chord4, chord4_2, chord4_3, chord4_4,
                    chord5, chord5_2, chord5_3, chord5_4,
                    chord6, chord6_2, chord6_3, chord6_4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, G, Ab, A, Bb, B, C
# Motif: F - Ab - Bb - C
note1 = pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75)  # F
note2 = pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0)  # Ab
note3 = pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25)  # Bb
note4 = pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5)  # C

note5 = pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.25)  # F
note6 = pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.5)  # Ab
note7 = pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75)  # Bb
note8 = pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0)  # C

note9 = pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.75)  # F
note10 = pretty_midi.Note(velocity=110, pitch=60, start=4.75, end=5.0)  # Ab
note11 = pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25)  # Bb
note12 = pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5)  # C

sax.notes.extend([note1, note2, note3, note4,
                  note5, note6, note7, note8,
                  note9, note10, note11, note12])

# Drums in bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo.mid")
