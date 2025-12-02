
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
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line, chromatic approaches)
bass_notes = [
    (19, 1.5), (18, 1.875), (20, 2.25), (21, 2.625),
    (22, 3.0), (21, 3.375), (20, 3.75), (19, 4.125),
    (18, 4.5), (17, 4.875), (19, 5.25), (20, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane on piano (7th chords, comp on 2 and 4)
piano_notes = [
    (50, 2.0), (53, 2.0), (57, 2.0), (60, 2.0),  # Fm7
    (54, 3.0), (57, 3.0), (60, 3.0), (64, 3.0),  # Bb7
    (50, 4.0), (53, 4.0), (57, 4.0), (60, 4.0)   # Fm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Little Ray on drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    bar_start = 1.5 * bar
    kick_time = bar_start
    snare_time = bar_start + 0.375
    hihat_time = bar_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125))
    for i in range(0, 4):
        hihat_note = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.125)
        drums.notes.append(hihat_note)

# Dante on sax (motif: F Bb Eb Ab, start on beat 2 of bar 2, leave it hanging)
sax_notes = [
    (53, 2.375), (50, 2.75), (48, 3.125), (45, 3.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Repeat the motif in bar 4, finishing it
sax_notes = [
    (53, 4.375), (50, 4.75), (48, 5.125), (45, 5.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
