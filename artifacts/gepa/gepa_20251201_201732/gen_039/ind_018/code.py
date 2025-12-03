
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = []
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass - walking line with chromatic approaches
bass_notes = []
for bar in range(2, 5):
    time = (bar - 1) * 1.5
    if bar == 2:
        # D2 -> Eb2 -> F2 -> G2
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=39, start=time + 0.375, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=41, start=time + 0.75, end=time + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=time + 1.125, end=time + 1.5))
    elif bar == 3:
        # G2 -> Ab2 -> Bb2 -> C3
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=time, end=time + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=44, start=time + 0.375, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=45, start=time + 0.75, end=time + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=48, start=time + 1.125, end=time + 1.5))
    elif bar == 4:
        # C3 -> D3 -> Eb3 -> F3
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=48, start=time, end=time + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=50, start=time + 0.375, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=51, start=time + 0.75, end=time + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=53, start=time + 1.125, end=time + 1.5))

bass.notes.extend(bass_notes)

# Diane on piano - open voicings, different chord each bar, resolve on last
piano_notes = []
for bar in range(2, 5):
    time = (bar - 1) * 1.5
    if bar == 2:
        # Dm7: D - F - A - C
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=62, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=64, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=67, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=69, start=time, end=time + 0.75))
    elif bar == 3:
        # G7: G - B - D - F
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=71, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=74, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=76, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=78, start=time, end=time + 0.75))
    elif bar == 4:
        # Cm7: C - Eb - G - Bb
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=60, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=63, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=67, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=95, pitch=71, start=time, end=time + 0.75))

piano.notes.extend(piano_notes)

# Little Ray on drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    time = (bar - 1) * 1.5
    for beat in range(4):
        beat_time = time + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=beat_time, end=beat_time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat_time, end=beat_time + 0.125))
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=beat_time, end=beat_time + 0.125))

drums.notes.extend(drum_notes)

# Dante on sax - short motif, one phrase, leave it hanging
sax_notes = []
time = 1.5  # start of bar 2
# Dm7 -> G7 -> Cm7
# Notes: D, F, A, Bb
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.375))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=time + 0.375, end=time + 0.75))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=time + 0.75, end=time + 1.125))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time + 1.125, end=time + 1.5))

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
