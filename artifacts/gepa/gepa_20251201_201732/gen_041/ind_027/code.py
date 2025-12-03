
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on beat 1
    (38, 0.75, 0.375),  # Snare on beat 2
    (36, 1.125, 0.375), # Kick on beat 3
    (38, 1.5, 0.375)    # Snare on beat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2
    (40, 1.875, 0.375), # Eb2 (chromatic approach)
    (43, 2.25, 0.375),  # G2
    (38, 2.625, 0.375)  # D2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F#-A-D-F)
piano_notes = [
    (62, 1.5, 0.375),  # F#
    (64, 1.5, 0.375),  # A
    (67, 1.5, 0.375),  # D
    (69, 1.5, 0.375),  # F
    (62, 1.875, 0.375), # F#
    (67, 1.875, 0.375), # D
    (64, 2.25, 0.375),  # A
    (69, 2.25, 0.375),  # F
    (62, 2.625, 0.375), # F#
    (64, 2.625, 0.375), # A
    (67, 2.625, 0.375), # D
    (69, 2.625, 0.375)  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on beat 1
    (42, 1.5, 0.1875), # Hihat on 1
    (42, 1.6875, 0.1875), # Hihat on &1
    (38, 1.875, 0.375),  # Snare on beat 2
    (42, 1.875, 0.1875), # Hihat on 2
    (42, 2.0625, 0.1875), # Hihat on &2
    (36, 2.25, 0.375),  # Kick on beat 3
    (42, 2.25, 0.1875), # Hihat on 3
    (42, 2.4375, 0.1875), # Hihat on &3
    (38, 2.625, 0.375),  # Snare on beat 4
    (42, 2.625, 0.1875), # Hihat on 4
    (42, 2.8125, 0.1875) # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 3.0, 0.375),  # D2
    (40, 3.375, 0.375), # Eb2 (chromatic approach)
    (43, 3.75, 0.375),  # G2
    (38, 4.125, 0.375)  # D2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Dm7 (F#-A-D-F)
piano_notes = [
    (62, 3.0, 0.375),  # F#
    (64, 3.0, 0.375),  # A
    (67, 3.0, 0.375),  # D
    (69, 3.0, 0.375),  # F
    (62, 3.375, 0.375), # F#
    (67, 3.375, 0.375), # D
    (64, 3.75, 0.375),  # A
    (69, 3.75, 0.375),  # F
    (62, 4.125, 0.375), # F#
    (64, 4.125, 0.375), # A
    (67, 4.125, 0.375), # D
    (69, 4.125, 0.375)  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on beat 1
    (42, 3.0, 0.1875), # Hihat on 1
    (42, 3.1875, 0.1875), # Hihat on &1
    (38, 3.375, 0.375),  # Snare on beat 2
    (42, 3.375, 0.1875), # Hihat on 2
    (42, 3.5625, 0.1875), # Hihat on &2
    (36, 3.75, 0.375),  # Kick on beat 3
    (42, 3.75, 0.1875), # Hihat on 3
    (42, 3.9375, 0.1875), # Hihat on &3
    (38, 4.125, 0.375),  # Snare on beat 4
    (42, 4.125, 0.1875), # Hihat on 4
    (42, 4.3125, 0.1875) # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 4.5, 0.375),  # D2
    (40, 4.875, 0.375), # Eb2 (chromatic approach)
    (43, 5.25, 0.375),  # G2
    (38, 5.625, 0.375)  # D2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 (F#-A-D-F)
piano_notes = [
    (62, 4.5, 0.375),  # F#
    (64, 4.5, 0.375),  # A
    (67, 4.5, 0.375),  # D
    (69, 4.5, 0.375),  # F
    (62, 4.875, 0.375), # F#
    (67, 4.875, 0.375), # D
    (64, 5.25, 0.375),  # A
    (69, 5.25, 0.375),  # F
    (62, 5.625, 0.375), # F#
    (64, 5.625, 0.375), # A
    (67, 5.625, 0.375), # D
    (69, 5.625, 0.375)  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on beat 1
    (42, 4.5, 0.1875), # Hihat on 1
    (42, 4.6875, 0.1875), # Hihat on &1
    (38, 4.875, 0.375),  # Snare on beat 2
    (42, 4.875, 0.1875), # Hihat on 2
    (42, 5.0625, 0.1875), # Hihat on &2
    (36, 5.25, 0.375),  # Kick on beat 3
    (42, 5.25, 0.1875), # Hihat on 3
    (42, 5.4375, 0.1875), # Hihat on &3
    (38, 5.625, 0.375),  # Snare on beat 4
    (42, 5.625, 0.1875), # Hihat on 4
    (42, 5.8125, 0.1875) # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Sax motif — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7: D-F-A-C (MIDI 67, 69, 71, 72)
sax_notes = [
    (67, 1.5, 0.375),  # D
    (69, 1.875, 0.375), # F
    (71, 2.25, 0.375),  # A
    (67, 2.625, 0.375), # D
    (69, 3.0, 0.375),  # F
    (71, 3.375, 0.375), # A
    (72, 3.75, 0.375),  # C
    (67, 4.125, 0.375), # D
    (69, 4.5, 0.375),  # F
    (71, 4.875, 0.375), # A
    (67, 5.25, 0.375),  # D
    (69, 5.625, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
