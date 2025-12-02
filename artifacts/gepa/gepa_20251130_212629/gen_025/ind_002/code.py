
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
    (36, 1.0),  # Kick on beat 1
    (38, 1.25), # Snare on beat 2
    (42, 1.0),  # Hihat on beat 1
    (42, 1.25), # Hihat on beat 2
    (42, 1.5),  # Hihat on beat 3
    (36, 1.5),  # Kick on beat 3
    (38, 1.75), # Snare on beat 4
    (42, 1.75), # Hihat on beat 4
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (29, 1.5),  # F (root)
    (30, 1.75), # Gb (chromatic)
    (31, 2.0),  # G (3rd)
    (32, 2.25), # Ab (chromatic)
    (33, 2.5),  # A (5th)
    (34, 2.75), # Bb (chromatic)
    (35, 3.0),  # B (7th)
    (36, 3.25), # C (octave)
    (37, 3.5),  # C# (chromatic)
    (38, 3.75), # D (9th)
    (39, 4.0),  # Eb (chromatic)
    (40, 4.25), # E (11th)
    (41, 4.5),  # F (root)
    (42, 4.75), # F# (chromatic)
    (43, 5.0),  # G (3rd)
    (44, 5.25)  # Ab (chromatic)
]

for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (45, 2.0),  # C7 (C, E, Bb)
    (48, 2.0),
    (50, 2.0),
    (52, 2.0),
    (45, 3.0),
    (48, 3.0),
    (50, 3.0),
    (52, 3.0),
    (55, 4.0),  # F7 (F, A, C)
    (57, 4.0),
    (59, 4.0),
    (60, 4.0)
]

for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax: Melody - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F G A Bb (1.5 - 1.75)
# Rest (1.75 - 2.0)
# F G A Bb (3.0 - 3.25)
# Rest (3.25 - 3.5)
# F G (4.0 - 4.25) - ends on a question

sax_notes = [
    (45, 1.5),  # F
    (46, 1.625), # G
    (47, 1.75),  # A
    (48, 1.875), # Bb
    (45, 3.0),  # F
    (46, 3.125), # G
    (47, 3.25),  # A
    (48, 3.375), # Bb
    (45, 4.0),  # F
    (46, 4.125)  # G
]

for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# Add rests to create tension and space
sax_rests = [
    (1.75, 2.0),
    (3.25, 3.5)
]

for start, end in sax_rests:
    sax_rest = pretty_midi.Note(velocity=0, pitch=45, start=start, end=end)
    sax.notes.append(sax_rest)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
