
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# Fm7: F, Ab, Bb, D
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5), # F#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.25), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5), # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75), # F#
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0), # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25), # F
    pretty_midi.Note(velocity=100, pitch=63, start=4.25, end=4.5), # Eb
    # Bar 4 (last 1.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.5), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 = F, Ab, Bb, D
# Bb7 = Bb, D, F, Ab
# Fm7 = F, Ab, Bb, D
# C7 = C, E, G, Bb
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0), # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0), # F#
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5), # F#
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5), # F
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.5), # G
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.0), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0), # F#
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.0), # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=4.25, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5), # F#
    pretty_midi.Note(velocity=100, pitch=68, start=4.25, end=4.5), # F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, G
# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=84, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=110, pitch=82, start=1.75, end=2.0), # Ab
    pretty_midi.Note(velocity=110, pitch=81, start=2.0, end=2.25), # Bb
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=87, start=2.25, end=2.75), # G
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=84, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=110, pitch=82, start=3.25, end=3.5), # Ab
    pretty_midi.Note(velocity=110, pitch=81, start=3.5, end=3.75), # Bb
    pretty_midi.Note(velocity=110, pitch=87, start=3.75, end=4.0), # G
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=84, start=4.25, end=4.5), # F
    pretty_midi.Note(velocity=110, pitch=82, start=4.5, end=4.75), # Ab
    pretty_midi.Note(velocity=110, pitch=81, start=4.75, end=5.0), # Bb
    pretty_midi.Note(velocity=110, pitch=87, start=5.0, end=5.5), # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
