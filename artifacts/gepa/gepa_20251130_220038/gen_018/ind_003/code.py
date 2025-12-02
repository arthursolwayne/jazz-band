
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

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
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bars 2-4: 4.5 seconds total
# Start at 1.5s
start_time = 1.5

# Bass line: walking line, chromatic approaches, no repeated notes
# F7 chord: F, A, C, E
# Walking bass line: F, G#, A, Bb, B, C, D, Eb, E, F#, G, Ab, A, Bb, B, C
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=start_time, end=start_time + 0.375), # F
    pretty_midi.Note(velocity=100, pitch=73, start=start_time + 0.375, end=start_time + 0.75), # G#
    pretty_midi.Note(velocity=100, pitch=72, start=start_time + 0.75, end=start_time + 1.125), # A
    pretty_midi.Note(velocity=100, pitch=71, start=start_time + 1.125, end=start_time + 1.5), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=start_time + 1.5, end=start_time + 1.875), # B
    pretty_midi.Note(velocity=100, pitch=71, start=start_time + 1.875, end=start_time + 2.25), # C
    pretty_midi.Note(velocity=100, pitch=74, start=start_time + 2.25, end=start_time + 2.625), # D
    pretty_midi.Note(velocity=100, pitch=70, start=start_time + 2.625, end=start_time + 3.0), # Eb
    pretty_midi.Note(velocity=100, pitch=72, start=start_time + 3.0, end=start_time + 3.375), # E
    pretty_midi.Note(velocity=100, pitch=76, start=start_time + 3.375, end=start_time + 3.75), # F#
    pretty_midi.Note(velocity=100, pitch=72, start=start_time + 3.75, end=start_time + 4.125), # G
    pretty_midi.Note(velocity=100, pitch=70, start=start_time + 4.125, end=start_time + 4.5), # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=start_time + 4.5, end=start_time + 4.875), # A
    pretty_midi.Note(velocity=100, pitch=71, start=start_time + 4.875, end=start_time + 5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=start_time + 5.25, end=start_time + 5.625), # B
    pretty_midi.Note(velocity=100, pitch=71, start=start_time + 5.625, end=start_time + 6.0), # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# F7 = F, A, C, E
# F7sus4 = F, Bb, C, E
# F7alt = F, Ab, C, Eb
# Comp on 2 and 4
piano_notes = []
# Bar 2 (1.5-3.0s): F7
# 2 and 4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 0.375, end=1.5 + 0.75)) # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=73, start=1.5 + 0.375, end=1.5 + 0.75)) # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5 + 0.375, end=1.5 + 0.75)) # E

# Bar 3 (3.0-4.5s): F7sus4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0 + 0.375, end=3.0 + 0.75)) # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.0 + 0.375, end=3.0 + 0.75)) # Bb
piano_notes.append(pretty_midi.Note(velocity=100, pitch=73, start=3.0 + 0.375, end=3.0 + 0.75)) # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.0 + 0.375, end=3.0 + 0.75)) # E

# Bar 4 (4.5-6.0s): F7alt
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5 + 0.375, end=4.5 + 0.75)) # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5 + 0.375, end=4.5 + 0.75)) # Ab
piano_notes.append(pretty_midi.Note(velocity=100, pitch=73, start=4.5 + 0.375, end=4.5 + 0.75)) # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5 + 0.375, end=4.5 + 0.75)) # Eb

piano.notes.extend(piano_notes)

# Sax: short motif, start it, leave it hanging, come back and finish it
# Motif: F, Bb, C, F (F7 chord, but with a twist)
# First note: F (bar 2 start)
note1 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375) # F
note2 = pretty_midi.Note(velocity=100, pitch=70, start=1.5 + 0.75, end=1.5 + 1.125) # Bb
note3 = pretty_midi.Note(velocity=100, pitch=73, start=1.5 + 1.5, end=1.5 + 1.875) # C
note4 = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 2.625, end=1.5 + 3.0) # F
sax.notes.extend([note1, note2, note3, note4])

# Drums: same pattern as bar 1, repeated for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
