
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
drum_notes = []
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F, Ab, D, Eb, etc.)
bass_notes = []
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Roots and fifths with chromatic approaches
    if bar == 2:
        # Fm - F and C
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=start + 0.0, end=start + 0.375))  # F (71)
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=start + 0.375, end=start + 0.75))  # C (76)
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=start + 0.75, end=start + 1.125))  # Eb (70)
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=start + 1.125, end=start + 1.5))  # F (71)
    elif bar == 3:
        # Abm - Ab and Eb
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=68, start=start + 0.0, end=start + 0.375))  # Ab (68)
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=73, start=start + 0.375, end=start + 0.75))  # Eb (73)
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=start + 0.75, end=start + 1.125))  # Gb (67)
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=68, start=start + 1.125, end=start + 1.5))  # Ab (68)
    elif bar == 4:
        # Dm - D and A
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=start + 0.0, end=start + 0.375))  # D (62)
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=start + 0.375, end=start + 0.75))  # A (67)
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=61, start=start + 0.75, end=start + 1.125))  # C (61)
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=start + 1.125, end=start + 1.5))  # D (62)

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = []
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    if bar == 2:
        # Fm7: F, Ab, C, Eb
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=68, start=start, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=start, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=70, start=start, end=start + 1.5))
    elif bar == 3:
        # Abm7: Ab, Db, Eb, Gb
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=68, start=start, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=73, start=start, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 1.5))
    elif bar == 4:
        # Dm7: D, F, A, C
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 1.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=start, end=start + 1.5))

piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = []
# Bar 2: Start the motif
start = 1.5
# F (71), Ab (68), D (62), F (71)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=start + 0.0, end=start + 0.375))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=68, start=start + 0.375, end=start + 0.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=start + 0.75, end=start + 1.125))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=start + 1.125, end=start + 1.5))

# Bar 3: Leave it hanging
# No notes here

# Bar 4: Come back and finish it
start = 3.0
sax_notes.append(pretty_midi.Note(velocity=110, pitch=68, start=start + 0.0, end=start + 0.375))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=start + 0.375, end=start + 0.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=start + 0.75, end=start + 1.125))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=76, start=start + 1.125, end=start + 1.5))

sax.notes.extend(sax_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
