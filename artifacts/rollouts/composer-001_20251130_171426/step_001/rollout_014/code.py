
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches
# Dm7: D F A C
bass_notes = [
    (1.5, 50), (1.75, 49), (2.0, 50), (2.25, 52),
    (2.5, 52), (2.75, 50), (3.0, 49), (3.25, 50),
    (3.5, 52), (3.75, 54), (4.0, 52), (4.25, 50),
    (4.5, 50), (4.75, 49), (5.0, 50), (5.25, 52)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 62), (2.0, 67), (2.0, 70), (2.0, 74),  # D7
    (2.5, 62), (2.5, 67), (2.5, 70), (2.5, 74),
    # Bar 3
    (3.0, 62), (3.0, 67), (3.0, 70), (3.0, 74),
    (3.5, 62), (3.5, 67), (3.5, 70), (3.5, 74),
    # Bar 4
    (4.0, 62), (4.0, 67), (4.0, 70), (4.0, 74),
    (4.5, 62), (4.5, 67), (4.5, 70), (4.5, 74)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick_times = [bar_start, bar_start + 0.75]
    snare_times = [bar_start + 0.375, bar_start + 1.125]
    hihat_times = [bar_start + i * 0.375 for i in range(4)]
    for time in kick_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    for time in snare_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    for time in hihat_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D - Eb - F - D (suspense), then resolve to G - A - Bb - D
sax_notes = [
    # First pass (Bar 2)
    (2.0, 62), (2.25, 60), (2.5, 64), (2.75, 62),
    # Second pass (Bar 4)
    (4.0, 67), (4.25, 69), (4.5, 67), (4.75, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
