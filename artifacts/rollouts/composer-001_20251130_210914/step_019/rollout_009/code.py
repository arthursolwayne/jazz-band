
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
for bar in range(1):
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on beat 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, never the same note twice
# D minor scale: D, Eb, F, G, Ab, Bb, C
# Start on D, walk with chromatic passing tones
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375), # Ab
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0), # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# D7 = D, F#, A, C
# Comp on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=95, pitch=62, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.125, end=4.5), # A
    pretty_midi.Note(velocity=95, pitch=64, start=4.125, end=4.5), # F#
    pretty_midi.Note(velocity=95, pitch=69, start=4.125, end=4.5), # C
]
piano.notes.extend(piano_notes)

# Drums: continue pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on beat 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif in D minor: D, Eb, F, G, Ab (chromatic)
# Start on D, leave it hanging on Eb, come back on F, end on G
sax_notes = [
    pretty_midi.Note(velocity=115, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=115, pitch=63, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=115, pitch=65, start=2.25, end=2.375), # F
    pretty_midi.Note(velocity=115, pitch=67, start=2.375, end=2.5), # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
