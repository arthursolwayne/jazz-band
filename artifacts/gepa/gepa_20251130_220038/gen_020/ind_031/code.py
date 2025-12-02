
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.75),  # Kick on 1
    (42, 0.0, 0.25),  # Hihat on 1
    (38, 0.75, 0.75), # Snare on 2
    (42, 0.75, 0.25), # Hihat on 2
    (36, 1.25, 0.75), # Kick on 3
    (42, 1.25, 0.25), # Hihat on 3
    (38, 1.5, 0.75),  # Snare on 4
    (42, 1.5, 0.25)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm
bass_notes = [
    (62, 1.5, 0.375), # D (beat 1)
    (60, 1.875, 0.375), # C (beat 2)
    (62, 2.25, 0.375), # D (beat 3)
    (64, 2.625, 0.375), # E (beat 4)
    (64, 2.625, 0.375), # E (beat 1)
    (62, 2.625, 0.375), # D (beat 2)
    (60, 2.625, 0.375), # C (beat 3)
    (62, 2.625, 0.375), # D (beat 4)
    (62, 3.0, 0.375), # D (beat 1)
    (60, 3.375, 0.375), # C (beat 2)
    (62, 3.75, 0.375), # D (beat 3)
    (64, 4.125, 0.375), # E (beat 4)
    (64, 4.125, 0.375), # E (beat 1)
    (62, 4.125, 0.375), # D (beat 2)
    (60, 4.125, 0.375), # C (beat 3)
    (62, 4.125, 0.375), # D (beat 4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 2.25, 0.375), # D7 (beat 3)
    (62, 2.625, 0.375), # D7 (beat 4)
    (62, 3.75, 0.375), # D7 (beat 3)
    (62, 4.125, 0.375), # D7 (beat 4)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif
sax_notes = [
    (62, 1.5, 0.375), # D (beat 1)
    (64, 1.875, 0.375), # E (beat 2)
    (62, 2.25, 0.375), # D (beat 3)
    (60, 2.625, 0.375), # C (beat 4)
    (62, 3.0, 0.375), # D (beat 1)
    (64, 3.375, 0.375), # E (beat 2)
    (62, 3.75, 0.375), # D (beat 3)
    (60, 4.125, 0.375)  # C (beat 4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    for beat in range(4):
        start = 1.5 + (bar - 2) * 1.5 + beat * 0.75
        if beat == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.75))
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.25))
        elif beat == 1:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.75))
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.25))
        elif beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.75))
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.25))
        elif beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.75))
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
