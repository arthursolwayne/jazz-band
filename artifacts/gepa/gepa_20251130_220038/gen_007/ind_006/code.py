
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36),  # Kick on 1
    (0.375, 42), # Hihat on 1&
    (0.75, 38),  # Snare on 2
    (1.125, 42), # Hihat on 2&
    (1.5, 36),   # Kick on 3
    (1.875, 42), # Hihat on 3&
    (2.25, 38),  # Snare on 4
    (2.625, 42)  # Hihat on 4&
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 64),  # F (root)
    (1.75, 65),  # Gb (chromatic approach)
    (2.0, 62),  # Eb (3rd)
    (2.25, 63), # E (chromatic approach)
    (2.5, 60),  # D (5th)
    (2.75, 59), # Db (chromatic approach)
    (3.0, 57),  # C (7th)
    (3.25, 58), # C# (chromatic approach)
    (3.5, 64),  # F (root)
    (3.75, 65),  # Gb (chromatic approach)
    (4.0, 62),  # Eb (3rd)
    (4.25, 63), # E (chromatic approach)
    (4.5, 60),  # D (5th)
    (4.75, 59), # Db (chromatic approach)
    (5.0, 57),  # C (7th)
    (5.25, 58)  # C# (chromatic approach)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    (2.0, 64),  # F7: F, A, C, Eb
    (2.0, 69),  # A
    (2.0, 60),  # C
    (2.0, 62),  # Eb
    (2.5, 64),  # F
    (2.5, 69),  # A
    (2.5, 60),  # C
    (2.5, 62),  # Eb
    (3.0, 64),  # F
    (3.0, 69),  # A
    (3.0, 60),  # C
    (3.0, 62),  # Eb
    (3.5, 64),  # F
    (3.5, 69),  # A
    (3.5, 60),  # C
    (3.5, 62)   # Eb
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66),  # F#
    (1.75, 64), # F
    (2.0, 62),  # Eb
    (2.25, 64), # F
    (2.5, 66),  # F#
    (2.75, 64), # F
    (3.0, 62),  # Eb
    (3.25, 64), # F
    (3.5, 66),  # F#
    (3.75, 64), # F
    (4.0, 62),  # Eb
    (4.25, 64), # F
    (4.5, 66),  # F#
    (4.75, 64), # F
    (5.0, 62),  # Eb
    (5.25, 64)  # F
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_start = 1.5
for bar in range(2, 5):
    for beat in range(4):
        time = bar_start + (beat * 0.375)
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        elif beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
