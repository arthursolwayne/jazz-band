
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
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=39, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=100, pitch=39, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping on beats 2 and 4
# Fm7 on beat 2, Am7 on beat 4 (bar 2)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75), # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # G
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - Bb - rest, then repeat an octave higher
# Bar 2: F, Ab (beat 1), Bb (beat 2)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=41, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=43, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=110, pitch=45, start=2.25, end=2.625), # Bb
    # Bar 3: Rest until beat 3
    pretty_midi.Note(velocity=110, pitch=53, start=3.375, end=3.75), # F (octave)
    pretty_midi.Note(velocity=110, pitch=55, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=110, pitch=57, start=4.125, end=4.5), # Bb
    # Bar 4: End on D (tension)
    pretty_midi.Note(velocity=110, pitch=40, start=4.5, end=4.875), # D (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Continue the pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_intro.mid")
