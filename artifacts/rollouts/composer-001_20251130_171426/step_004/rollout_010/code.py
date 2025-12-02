
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
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    kick = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=i * 1.5,
        end=i * 1.5 + 0.375
    )
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    snare = pretty_midi.Note(
        velocity=110,
        pitch=note,
        start=i * 1.5,
        end=i * 1.5 + 0.375
    )
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    hihat = pretty_midi.Note(
        velocity=80,
        pitch=note,
        start=i * 0.375,
        end=i * 0.375 + 0.125
    )
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    62,  # D
    64,  # Eb
    65,  # E
    67,  # F
    69,  # G
    71,  # Ab
    72,  # A
    74,  # Bb
    76,  # B
    77,  # C
    79,  # C#
    81,  # D
    83,  # Eb
    84,  # E
    86,  # F
    88   # G
]

for i, note in enumerate(bass_notes):
    bass_note = pretty_midi.Note(
        velocity=80,
        pitch=note,
        start=i * 0.375 + 1.5,
        end=i * 0.375 + 1.5 + 0.25
    )
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
chords = [
    (67, 71, 74, 76),  # D7
    (67, 71, 74, 76),  # D7
    (69, 73, 76, 79),  # E7
    (69, 73, 76, 79),  # E7
    (67, 71, 74, 76),  # D7
    (67, 71, 74, 76),  # D7
    (69, 73, 76, 79),  # E7
    (69, 73, 76, 79),  # E7
    (67, 71, 74, 76),  # D7
    (67, 71, 74, 76),  # D7
    (69, 73, 76, 79),  # E7
    (69, 73, 76, 79),  # E7
    (67, 71, 74, 76),  # D7
    (67, 71, 74, 76),  # D7
    (69, 73, 76, 79),  # E7
    (69, 73, 76, 79)   # E7
]

for i, chord in enumerate(chords):
    for note in chord:
        piano_note = pretty_midi.Note(
            velocity=100,
            pitch=note,
            start=i * 0.375 + 1.5,
            end=i * 0.375 + 1.5 + 0.25
        )
        piano.notes.append(piano_note)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (67, 1.5, 1.75),     # D
    (71, 1.75, 2.0),     # G
    (76, 2.0, 2.25),     # B
    (71, 2.25, 2.5),     # G
    (67, 2.5, 2.75),     # D
    (76, 2.75, 3.0),     # B
    (79, 3.0, 3.25),     # C#
    (76, 3.25, 3.5),     # B
    (79, 3.5, 3.75),     # C#
    (76, 3.75, 4.0),     # B
    (74, 4.0, 4.25),     # A
    (76, 4.25, 4.5),     # B
    (71, 4.5, 4.75),     # G
    (67, 4.75, 5.0),     # D
    (74, 5.0, 5.25),     # A
    (71, 5.25, 5.5),     # G
    (67, 5.5, 5.75),     # D
    (69, 5.75, 6.0)      # E
]

for note, start, end in sax_notes:
    sax_note = pretty_midi.Note(
        velocity=110,
        pitch=note,
        start=start,
        end=end
    )
    sax.notes.append(sax_note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
