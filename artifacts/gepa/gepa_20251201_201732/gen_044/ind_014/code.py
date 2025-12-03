
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),  # Snare on 4
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Fm root (F), chromatic approach to Gm (F, Eb, G)
note1 = pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75)  # F (root)
note2 = pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0)  # Eb (chromatic approach)
note3 = pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25)  # F again
note4 = pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5)  # G (root of Gm)
note5 = pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75)  # F
note6 = pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0)  # G
bass.notes.extend([note1, note2, note3, note4, note5, note6])

# Piano: Open voicing, Fm7 (F, Ab, C, Eb) on bar 2, then Gm7 (G, Bb, D, F)
# Comp on 2 and 4
note1 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0)  # F
note2 = pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.0)  # Ab
note3 = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0)  # C
note4 = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0)  # Eb
note5 = pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0)  # G
note6 = pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=3.0)  # Bb
note7 = pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0)  # D
note8 = pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0)  # F
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Sax: One short motif, start on beat 1, leave it hanging
note1 = pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.75)  # Bb (Fm scale)
note2 = pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0)  # Eb (chromatic)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25)  # Bb
note4 = pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5)  # D (tension)
note5 = pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75)  # Bb
note6 = pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0)  # Eb
sax.notes.extend([note1, note2, note3, note4, note5, note6])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Fm root (F), chromatic approach to Cm (F, Eb, D)
note1 = pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25)  # F
note2 = pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5)  # Eb
note3 = pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75)  # D
note4 = pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0)  # Eb
note5 = pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25)  # F
note6 = pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5)  # D
bass.notes.extend([note1, note2, note3, note4, note5, note6])

# Piano: Open voicing, Cm7 (C, Eb, G, Bb) on bar 3, then Fm7 (F, Ab, C, Eb)
# Comp on 2 and 4
note1 = pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5)  # C
note2 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5)  # Eb
note3 = pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5)  # G
note4 = pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.5)  # Bb
note5 = pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.5)  # F
note6 = pretty_midi.Note(velocity=100, pitch=68, start=4.0, end=4.5)  # Ab
note7 = pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.5)  # C
note8 = pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.5)  # Eb
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Sax: Motif variation, answer the question from bar 2
note1 = pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.25)  # C (answer)
note2 = pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5)  # Eb
note3 = pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75)  # C
note4 = pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0)  # Bb
note5 = pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.25)  # Eb
note6 = pretty_midi.Note(velocity=110, pitch=72, start=4.25, end=4.5)  # C
sax.notes.extend([note1, note2, note3, note4, note5, note6])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Fm root (F), chromatic approach to Fm (F, G, F)
note1 = pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75)  # F
note2 = pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0)  # G
note3 = pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25)  # F
note4 = pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.5)  # G
note5 = pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75)  # F
note6 = pretty_midi.Note(velocity=90, pitch=72, start=5.75, end=6.0)  # G
bass.notes.extend([note1, note2, note3, note4, note5, note6])

# Piano: Open voicing, Fm7 (F, Ab, C, Eb) on bar 4, resolve on the last beat
# Comp on 2 and 4
note1 = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0)  # F
note2 = pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=5.0)  # Ab
note3 = pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0)  # C
note4 = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0)  # Eb
note5 = pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=6.0)  # F
note6 = pretty_midi.Note(velocity=100, pitch=68, start=5.5, end=6.0)  # Ab
note7 = pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=6.0)  # C
note8 = pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=6.0)  # Eb
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Sax: Finale, bring the motif back and end it
note1 = pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75)  # Bb
note2 = pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0)  # Eb
note3 = pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25)  # Bb
note4 = pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5)  # D
note5 = pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75)  # Bb
note6 = pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0)  # Eb
sax.notes.extend([note1, note2, note3, note4, note5, note6])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
