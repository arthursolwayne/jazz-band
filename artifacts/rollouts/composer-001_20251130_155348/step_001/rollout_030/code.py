
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

# Bass line (Marcus): walking line with chromatic approaches
bass_notes = []
for bar in range(2, 5):
    time = (bar - 1) * 1.5
    if bar == 2:
        # Dm7 -> G7 -> Cmaj7 -> F7
        # D -> Eb -> G -> A -> B -> C -> D -> Eb
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time, end=time + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=63, start=time + 0.375, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + 0.75, end=time + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 1.125, end=time + 1.5))
    elif bar == 3:
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 0.375, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=time + 0.75, end=time + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=78, start=time + 1.125, end=time + 1.5))
    elif bar == 4:
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=80, start=time, end=time + 0.375))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=81, start=time + 0.375, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=84, start=time + 0.75, end=time + 1.125))
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=86, start=time + 1.125, end=time + 1.5))

bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = []
for bar in range(2, 5):
    time = (bar - 1) * 1.5
    if bar == 2:
        # Dm7: D, F, A, C
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time + 0.75, end=time + 0.875))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=time + 0.75, end=time + 0.875))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 0.75, end=time + 0.875))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time + 0.75, end=time + 0.875))
    elif bar == 3:
        # G7: G, B, D, F
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + 0.75, end=time + 0.875))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time + 0.75, end=time + 0.875))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=time + 0.75, end=time + 0.875))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=time + 0.75, end=time + 0.875))
    elif bar == 4:
        # Cmaj7: C, E, G, B
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=time + 0.75, end=time + 0.875))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=time + 0.75, end=time + 0.875))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + 0.75, end=time + 0.875))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time + 0.75, end=time + 0.875))

piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
time = 1.5
# First motif: D, F#, A, B (Dmaj7)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.375))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=time + 0.375, end=time + 0.75))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time + 0.75, end=time + 1.125))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 1.125, end=time + 1.5))
# Leave it hanging for a beat
# Then return with a variation: D, F#, Bb, D (D7)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time + 1.5, end=time + 1.875))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=time + 1.875, end=time + 2.25))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=70, start=time + 2.25, end=time + 2.625))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time + 2.625, end=time + 3.0))

sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    time = (bar - 1) * 1.5
    for beat in range(4):
        time_beat = time + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time_beat, end=time_beat + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time_beat, end=time_beat + 0.125))
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time_beat, end=time_beat + 0.125))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
