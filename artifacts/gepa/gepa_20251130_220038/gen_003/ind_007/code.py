
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

# Bass line (Marcus) - chromatic walking line starting on D (62)
bass_notes = [
    (62, 1.5), (63, 1.75), (61, 2.0), (60, 2.25),
    (62, 2.5), (63, 2.75), (61, 3.0), (60, 3.25),
    (62, 3.5), (63, 3.75), (61, 4.0), (60, 4.25),
    (62, 4.5), (63, 4.75), (61, 5.0), (60, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano (Diane) - 7th chords on 2 and 4, comping
piano_notes = []
# Bar 2
piano_notes.extend([
    (67, 2.0), (71, 2.0), (64, 2.0), (69, 2.0),
    (72, 2.5), (76, 2.5), (69, 2.5), (74, 2.5)
])
# Bar 3
piano_notes.extend([
    (67, 3.0), (71, 3.0), (64, 3.0), (69, 3.0),
    (72, 3.5), (76, 3.5), (69, 3.5), (74, 3.5)
])
# Bar 4
piano_notes.extend([
    (67, 4.0), (71, 4.0), (64, 4.0), (69, 4.0),
    (72, 4.5), (76, 4.5), (69, 4.5), (74, 4.5)
])
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append((36, start + 0.0))
    drum_notes.append((36, start + 0.75))
    # Snare on 2 and 4
    drum_notes.append((38, start + 0.375))
    drum_notes.append((38, start + 1.125))
    # Hihat on every eighth
    drum_notes.append((42, start + 0.0))
    drum_notes.append((42, start + 0.375))
    drum_notes.append((42, start + 0.75))
    drum_notes.append((42, start + 1.125))

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Saxophone (Dante) - motif in D, one short motive, leave it hanging
sax_notes = [
    (62, 1.5), (67, 1.875), (64, 2.25), (62, 2.5),
    (67, 2.75), (64, 3.125), (62, 3.5),
    (67, 3.75), (64, 4.125), (62, 4.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
