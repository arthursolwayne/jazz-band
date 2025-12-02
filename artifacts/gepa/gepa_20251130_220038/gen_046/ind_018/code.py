
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.375),
    (42, 0.75), (42, 1.125), (42, 1.5),
    (36, 1.5),
]

# Add the kick on 3rd beat
drum_notes.append((36, 1.125))

for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bassline: walking line in Fm with chromatic approaches
bass_notes = [
    # Bar 2
    (48, 1.5, 1.75), (49, 1.75, 2.0), (47, 2.0, 2.25), (50, 2.25, 2.5),
    # Bar 3
    (50, 2.5, 2.75), (51, 2.75, 3.0), (49, 3.0, 3.25), (52, 3.25, 3.5),
    # Bar 4
    (52, 3.5, 3.75), (53, 3.75, 4.0), (51, 4.0, 4.25), (54, 4.25, 4.5),
    # End with a half-step chromatic approach to F
    (53, 4.5, 4.75), (54, 4.75, 5.0)
]

for note, start, end in bass_notes:
    b = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(b)

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2
    (57, 1.75, 2.0), (60, 1.75, 2.0), (62, 1.75, 2.0), (64, 1.75, 2.0),  # Fm7
    # Bar 3
    (57, 3.0, 3.25), (60, 3.0, 3.25), (62, 3.0, 3.25), (64, 3.0, 3.25),  # Fm7
    # Bar 4
    (57, 4.25, 4.5), (60, 4.25, 4.5), (62, 4.25, 4.5), (64, 4.25, 4.5)   # Fm7
]

for note, start, end in piano_notes:
    p = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    piano.notes.append(p)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Fm scale: F, Gb, Ab, Bb, B, C, Db
# Motif: F -> Ab -> B -> F (half-step chromatic approach)
# Start on F, then Ab on the and of 2, B on the and of 3, resolve to F on beat 4

sax_notes = [
    (53, 1.5, 1.625),  # F
    (55, 1.75, 1.875),  # Ab
    (57, 2.125, 2.25),  # B
    (53, 2.5, 2.75),    # F
    (53, 3.5, 3.625),   # F again, delayed resolution
    (55, 3.75, 3.875),  # Ab
    (57, 4.125, 4.25),  # B
    (53, 4.5, 4.75)     # F
]

for note, start, end in sax_notes:
    s = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(s)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
