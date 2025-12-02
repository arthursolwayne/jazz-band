
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
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# Fm7: F, Ab, Bb, D
# Walking line: F, Gb, G, Ab, A, Bb, B, C, etc.

bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.5),  # Ab

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # C

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=73, start=3.5, end=3.75),  # C#
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=75, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=76, start=4.25, end=4.5),  # E

    # Bar 4 (cont)
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=78, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=90, pitch=79, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=80, start=5.25, end=5.5),  # G#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, D
# Bb7 = Bb, D, F, Ab
# D7 = D, F#, A, C
# Ab7 = Ab, C, Eb, G

# Bar 2: Fm7 on beat 2
chord_f7 = pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25)
chord_ab7 = pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.25)
chord_bb7 = pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.25)
chord_d7 = pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25)

# Bar 3: Bb7 on beat 4
chord_bb7 = pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.75)
chord_d7 = pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75)
chord_f7 = pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75)
chord_ab7 = pretty_midi.Note(velocity=90, pitch=76, start=3.5, end=3.75)

# Bar 4: D7 on beat 2
chord_d7 = pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25)
chord_f7 = pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25)
chord_ab7 = pretty_midi.Note(velocity=90, pitch=76, start=4.0, end=4.25)
chord_bb7 = pretty_midi.Note(velocity=90, pitch=70, start=4.0, end=4.25)

# Bar 4: Ab7 on beat 4
chord_ab7 = pretty_midi.Note(velocity=90, pitch=76, start=5.5, end=5.75)
chord_c7 = pretty_midi.Note(velocity=90, pitch=72, start=5.5, end=5.75)
chord_eb7 = pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75)
chord_g7 = pretty_midi.Note(velocity=90, pitch=75, start=5.5, end=5.75)

piano.notes.extend([chord_f7, chord_ab7, chord_bb7, chord_d7,
                    chord_bb7, chord_d7, chord_f7, chord_ab7,
                    chord_d7, chord_f7, chord_ab7, chord_bb7,
                    chord_ab7, chord_c7, chord_eb7, chord_g7])

# Sax: One short motif in Fm, make it sing
# F, Gb, Bb, Ab (motif)
# Start it, leave it hanging. Come back and finish it.

# Bar 2
note1 = pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75)  # F
note2 = pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0)  # Gb
note3 = pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25)  # Bb
note4 = pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.5)  # Ab

# Bar 3
note5 = pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=3.0)  # F (rest then repeat)
note6 = pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25)  # Gb
note7 = pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5)  # Bb
note8 = pretty_midi.Note(velocity=110, pitch=68, start=3.5, end=3.75)  # Ab

# Bar 4
note9 = pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0)  # F
note10 = pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25)  # Gb
note11 = pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5)  # Bb
note12 = pretty_midi.Note(velocity=110, pitch=68, start=4.5, end=4.75)  # Ab

sax.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8,
                  note9, note10, note11, note12])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
