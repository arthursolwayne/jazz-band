
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4, in F7 (F A C E♭)
# Bar 2: F7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # E♭
]

# Bar 3: F7 on beat 2
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # E♭
]

# Bar 4: F7 on beat 2
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # E♭
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax melody (start on beat 2 of bar 2)
# Whisper at first, cry at the end. One short motif, leave it hanging, come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    # Add to drum notes
    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
