
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

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        for eighth in range(2):
            drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = []
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    # F minor walking bass line: F, Gb, G, Ab, A, Bb, B, C
    # Repeating pattern with chromatic approach
    if bar == 2:
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=time + 0.375, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 0.75, end=time + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time + 1.125, end=time + 1.5))
    elif bar == 3:
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time, end=time + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time + 0.375, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=73, start=time + 0.75, end=time + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 1.125, end=time + 1.5))
    elif bar == 4:
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=73, start=time, end=time + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 0.375, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=time + 0.75, end=time + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=73, start=time + 1.125, end=time + 1.5))

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = []
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    # F7 on bar 2, Ab7 on bar 3, Bb7 on bar 4
    if bar == 2:
        # F7: F, A, C, Eb
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time + 0.75, end=time + 1.125))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=time + 0.75, end=time + 1.125))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=time + 0.75, end=time + 1.125))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=73, start=time + 0.75, end=time + 1.125))
    elif bar == 3:
        # Ab7: Ab, C, Eb, Gb
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=time + 0.75, end=time + 1.125))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=time + 0.75, end=time + 1.125))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=73, start=time + 0.75, end=time + 1.125))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time + 0.75, end=time + 1.125))
    elif bar == 4:
        # Bb7: Bb, D, F, Ab
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 0.75, end=time + 1.125))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=time + 0.75, end=time + 1.125))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=time + 0.75, end=time + 1.125))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=time + 0.75, end=time + 1.125))

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
time = 1.5
# Motif (F, Gb, A, Bb) - F6, Gb6, A6, Bb6
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time, end=time + 0.375))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=70, start=time + 0.375, end=time + 0.75))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=73, start=time + 0.75, end=time + 1.125))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=time + 1.125, end=time + 1.5))

# Repeat the motif to finish it
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 1.5, end=time + 1.875))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=70, start=time + 1.875, end=time + 2.25))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=73, start=time + 2.25, end=time + 2.625))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=time + 2.625, end=time + 3.0))

sax.notes.extend(sax_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    for beat in range(4):
        current_time = time + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=current_time, end=current_time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=current_time, end=current_time + 0.125))
        for eighth in range(2):
            drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=current_time + eighth * 0.1875, end=current_time + eighth * 0.1875 + 0.0625))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
