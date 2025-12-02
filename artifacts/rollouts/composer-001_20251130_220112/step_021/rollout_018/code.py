
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

# Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

drum_notes = []
for t in kick_times:
    drum_notes.append(pretty_midi.Note(100, 36, t, t + 0.125))
for t in snare_times:
    drum_notes.append(pretty_midi.Note(100, 38, t, t + 0.125))
for t in hihat_times:
    drum_notes.append(pretty_midi.Note(100, 42, t, t + 0.0625))
drums.notes.extend(drum_notes)

# Bar 2-4 (1.5s - 6.0s)
# Bass: walking line, chromatic approaches, never the same note twice
# Dm7 chord: D F A C
# Walking bass line in Dm
bass_notes = [
    # Bar 2
    pretty_midi.Note(100, 50, 1.5, 1.75),  # D
    pretty_midi.Note(100, 49, 1.75, 2.0),  # C
    pretty_midi.Note(100, 51, 2.0, 2.25),  # Eb
    pretty_midi.Note(100, 52, 2.25, 2.5),  # F
    # Bar 3
    pretty_midi.Note(100, 53, 2.5, 2.75),  # F#
    pretty_midi.Note(100, 52, 2.75, 3.0),  # F
    pretty_midi.Note(100, 50, 3.0, 3.25),  # D
    pretty_midi.Note(100, 49, 3.25, 3.5),  # C
    # Bar 4
    pretty_midi.Note(100, 51, 3.5, 3.75),  # Eb
    pretty_midi.Note(100, 52, 3.75, 4.0),  # F
    pretty_midi.Note(100, 54, 4.0, 4.25),  # G
    pretty_midi.Note(100, 52, 4.25, 4.5),  # F
    # Bar 4 continuation
    pretty_midi.Note(100, 50, 4.5, 4.75),  # D
    pretty_midi.Note(100, 49, 4.75, 5.0),  # C
    pretty_midi.Note(100, 51, 5.0, 5.25),  # Eb
    pretty_midi.Note(100, 52, 5.25, 5.5),  # F
    pretty_midi.Note(100, 53, 5.5, 5.75),  # F#
    pretty_midi.Note(100, 52, 5.75, 6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Bars 2-4
piano_notes = []
# Bar 2 (on 2 and 4)
piano_notes.append(pretty_midi.Note(80, 50, 1.75, 2.0))  # D
piano_notes.append(pretty_midi.Note(80, 53, 1.75, 2.0))  # F#
piano_notes.append(pretty_midi.Note(80, 57, 1.75, 2.0))  # A
piano_notes.append(pretty_midi.Note(80, 60, 1.75, 2.0))  # C
piano_notes.append(pretty_midi.Note(80, 50, 2.25, 2.5))  # D
piano_notes.append(pretty_midi.Note(80, 53, 2.25, 2.5))  # F#
piano_notes.append(pretty_midi.Note(80, 57, 2.25, 2.5))  # A
piano_notes.append(pretty_midi.Note(80, 60, 2.25, 2.5))  # C
# Bar 3
piano_notes.append(pretty_midi.Note(80, 50, 3.25, 3.5))  # D
piano_notes.append(pretty_midi.Note(80, 53, 3.25, 3.5))  # F#
piano_notes.append(pretty_midi.Note(80, 57, 3.25, 3.5))  # A
piano_notes.append(pretty_midi.Note(80, 60, 3.25, 3.5))  # C
piano_notes.append(pretty_midi.Note(80, 50, 3.75, 4.0))  # D
piano_notes.append(pretty_midi.Note(80, 53, 3.75, 4.0))  # F#
piano_notes.append(pretty_midi.Note(80, 57, 3.75, 4.0))  # A
piano_notes.append(pretty_midi.Note(80, 60, 3.75, 4.0))  # C
# Bar 4
piano_notes.append(pretty_midi.Note(80, 50, 4.75, 5.0))  # D
piano_notes.append(pretty_midi.Note(80, 53, 4.75, 5.0))  # F#
piano_notes.append(pretty_midi.Note(80, 57, 4.75, 5.0))  # A
piano_notes.append(pretty_midi.Note(80, 60, 4.75, 5.0))  # C
piano_notes.append(pretty_midi.Note(80, 50, 5.25, 5.5))  # D
piano_notes.append(pretty_midi.Note(80, 53, 5.25, 5.5))  # F#
piano_notes.append(pretty_midi.Note(80, 57, 5.25, 5.5))  # A
piano_notes.append(pretty_midi.Note(80, 60, 5.25, 5.5))  # C
piano_notes.append(pretty_midi.Note(80, 50, 5.75, 6.0))  # D
piano_notes.append(pretty_midi.Note(80, 53, 5.75, 6.0))  # F#
piano_notes.append(pretty_midi.Note(80, 57, 5.75, 6.0))  # A
piano_notes.append(pretty_midi.Note(80, 60, 5.75, 6.0))  # C
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D -> Eb -> F -> C (half note, quarter note, eighth note, eighth note)
# Then repeat with slight variation
sax_notes = [
    # Bar 2
    pretty_midi.Note(100, 50, 1.5, 2.0),  # D (half note)
    pretty_midi.Note(100, 51, 2.0, 2.25),  # Eb (eighth)
    pretty_midi.Note(100, 52, 2.25, 2.5),  # F (eighth)
    pretty_midi.Note(100, 60, 2.5, 3.0),  # C (quarter)
    # Bar 3
    pretty_midi.Note(100, 50, 3.0, 3.5),  # D (quarter)
    pretty_midi.Note(100, 51, 3.5, 3.75),  # Eb (eighth)
    pretty_midi.Note(100, 52, 3.75, 4.0),  # F (eighth)
    pretty_midi.Note(100, 57, 4.0, 4.5),  # A (quarter)
    # Bar 4
    pretty_midi.Note(100, 50, 4.5, 5.0),  # D (quarter)
    pretty_midi.Note(100, 51, 5.0, 5.25),  # Eb (eighth)
    pretty_midi.Note(100, 52, 5.25, 5.5),  # F (eighth)
    pretty_midi.Note(100, 60, 5.5, 6.0),  # C (quarter)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
