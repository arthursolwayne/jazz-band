
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
bar_length = 1.5  # in seconds
for beat in [0, 1, 2, 3]:
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (1.5, 62),   # D
    (1.875, 64),  # E
    (2.25, 63),   # Eb
    (2.625, 65),  # F
    (3.0, 67),    # G
    (3.375, 69),  # A
    (3.75, 68),   # Ab
    (4.125, 70),  # Bb
    (4.5, 72),    # B
    (4.875, 71),  # Bb
    (5.25, 69),   # A
    (5.625, 67),  # G
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 70), (1.5, 72),  # Dm7
    (2.25, 62), (2.25, 67), (2.25, 70), (2.25, 72),  # Dm7
    (3.0, 62), (3.0, 67), (3.0, 70), (3.0, 72),  # Dm7
    (3.75, 62), (3.75, 67), (3.75, 70), (3.75, 72),  # Dm7
    (4.5, 62), (4.5, 67), (4.5, 70), (4.5, 72),  # Dm7
    (5.25, 62), (5.25, 67), (5.25, 70), (5.25, 72),  # Dm7
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * bar_length
    for beat in [0, 1, 2, 3]:
        time = start + beat * 0.375
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.1)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.1)
            drums.notes.append(note)

# Sax: One short motif, make it sing
# Start on D, then Bb, then Eb, leave it hanging
sax_notes = [
    (1.5, 62),  # D (start)
    (1.875, 67),  # Bb
    (2.25, 64),  # Eb
    (2.625, 62),  # D (resolve)
    (3.0, 62),  # D (hold)
    (3.375, 62),  # D
    (3.75, 62),  # D
    (4.125, 62),  # D
    (4.5, 62),  # D
    (4.875, 62),  # D
    (5.25, 62),  # D
    (5.625, 62),  # D
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
