
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.tempo = 120  # BPM

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
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice.
# C minor walking bass line: C - Bb - B - C - D - Eb - E - D - C - Bb - B - C - D - Eb - E - D
bass_notes = [60, 61, 62, 60, 63, 64, 65, 63, 60, 61, 62, 60, 63, 64, 65, 63]
bass_times = [1.5 + i * 0.375 for i in range(len(bass_notes))]
for t, pitch in zip(bass_times, bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
# Cm7 on 2 and 4, comp with rootless voicings
chords = [
    # Bar 2 (1.5 - 2.0s): Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=63, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=2.0),
    # Bar 3 (2.5 - 3.0s): Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=63, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=70, start=2.5, end=3.0),
    # Bar 4 (3.5 - 4.0s): Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=4.0),
    pretty_midi.Note(velocity=90, pitch=63, start=3.5, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=4.0),
    pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=4.0),
]
for note in chords:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Cm motif: C - Eb - Bb - D - C (half note, quarter note, eighth note, eighth note, half note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.5),
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.5)
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_piece.mid')
