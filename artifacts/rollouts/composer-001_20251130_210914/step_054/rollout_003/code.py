
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
    start = bar * 1.5
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    drums.notes.append(kick)
    kick_time = start + 1.125
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = start + 0.75
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.375)
    drums.notes.append(snare)
    snare_time = start + 2.25
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat_time = start + i * 0.375
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.1875)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches, no repeated notes
# Fm: F, Ab, Bb, Db
for bar in range(2, 5):
    start = bar * 1.5
    # Bass line
    if bar == 2:
        # F -> Gb (chromatic approach) -> Ab -> A
        bass_notes = [pretty_midi.Note(velocity=90, pitch=53, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=90, pitch=54, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=90, pitch=55, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=90, pitch=56, start=start + 1.125, end=start + 1.5)]
    elif bar == 3:
        # Bb -> B -> C -> Db
        bass_notes = [pretty_midi.Note(velocity=90, pitch=50, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=90, pitch=51, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=90, pitch=52, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=90, pitch=53, start=start + 1.125, end=start + 1.5)]
    else:
        # F -> Gb -> Ab -> A
        bass_notes = [pretty_midi.Note(velocity=90, pitch=53, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=90, pitch=54, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=90, pitch=55, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=90, pitch=56, start=start + 1.125, end=start + 1.5)]
    for note in bass_notes:
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab
# E7 = E, G#, B, D
for bar in range(2, 5):
    start = bar * 1.5
    if bar % 2 == 0:
        # Bar 2 and 4: comp on 2 and 4
        # F7 on 2
        chord_notes = [pretty_midi.Note(velocity=95, pitch=53, start=start + 0.75, end=start + 1.125),
                       pretty_midi.Note(velocity=90, pitch=58, start=start + 0.75, end=start + 1.125),
                       pretty_midi.Note(velocity=85, pitch=55, start=start + 0.75, end=start + 1.125),
                       pretty_midi.Note(velocity=80, pitch=57, start=start + 0.75, end=start + 1.125)]
        for note in chord_notes:
            piano.notes.append(note)
        # Bb7 on 4
        if bar == 4:
            chord_notes = [pretty_midi.Note(velocity=95, pitch=50, start=start + 2.25, end=start + 2.625),
                           pretty_midi.Note(velocity=90, pitch=53, start=start + 2.25, end=start + 2.625),
                           pretty_midi.Note(velocity=85, pitch=55, start=start + 2.25, end=start + 2.625),
                           pretty_midi.Note(velocity=80, pitch=57, start=start + 2.25, end=start + 2.625)]
            for note in chord_notes:
                piano.notes.append(note)
    else:
        # Bar 3: comp on 2 and 4
        # E7 on 2
        chord_notes = [pretty_midi.Note(velocity=95, pitch=56, start=start + 0.75, end=start + 1.125),
                       pretty_midi.Note(velocity=90, pitch=60, start=start + 0.75, end=start + 1.125),
                       pretty_midi.Note(velocity=85, pitch=62, start=start + 0.75, end=start + 1.125),
                       pretty_midi.Note(velocity=80, pitch=65, start=start + 0.75, end=start + 1.125)]
        for note in chord_notes:
            piano.notes.append(note)
        # F7 on 4
        chord_notes = [pretty_midi.Note(velocity=95, pitch=53, start=start + 2.25, end=start + 2.625),
                       pretty_midi.Note(velocity=90, pitch=58, start=start + 2.25, end=start + 2.625),
                       pretty_midi.Note(velocity=85, pitch=55, start=start + 2.25, end=start + 2.625),
                       pretty_midi.Note(velocity=80, pitch=57, start=start + 2.25, end=start + 2.625)]
        for note in chord_notes:
            piano.notes.append(note)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F
# Bar 2: F (start), Ab (end of bar)
note1 = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.5 + 0.375)
sax.notes.append(note1)
note2 = pretty_midi.Note(velocity=100, pitch=55, start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note2)
# Bar 3: Bb (start), leave it hanging
note3 = pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.0 + 0.375)
sax.notes.append(note3)
# Bar 4: F (end of bar)
note4 = pretty_midi.Note(velocity=100, pitch=53, start=4.5 + 1.125, end=4.5 + 1.5)
sax.notes.append(note4)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    drums.notes.append(kick)
    kick_time = start + 1.125
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = start + 0.75
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.375)
    drums.notes.append(snare)
    snare_time = start + 2.25
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat_time = start + i * 0.375
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
